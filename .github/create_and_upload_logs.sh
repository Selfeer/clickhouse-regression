#!/bin/bash

set -x
sudo chown -R $(whoami):$(whoami) $SUITE/

if [[ $artifacts == 'internal' ]];
then
    artifact_s3_bucket_path="altinity-internal-test-reports"
    confidential="--confidential"
elif [[ $artifacts == 'public' ]];
then
    artifact_s3_bucket_path="altinity-test-reports"
    confidential=""
elif [[ $artifacts == 'builds' ]];
then
    artifact_s3_bucket_path="altinity-build-artifacts"
    confidential=""
    if [[ $event_name == "pull_request" ]];
    then
        artifact_s3_dir="PRs/$pr_number/$build_sha/regression"
    elif [[ $event_name == "release" ]];
    then
        artifact_s3_dir="0/$build_sha/regression"
    fi
    
fi

echo $version > version.log.txt
echo "https://gitlab.com/altinity-qa/clickhouse/cicd/clickhouse-regression/-/pipelines/$GITHUB_RUN_ID" > pipeline_url.log.txt
tfs --debug --no-colors transform compact raw.log compact.log
tfs --debug --no-colors transform nice raw.log nice.log.txt 
tfs --debug --no-colors transform short raw.log short.log.txt
tfs --debug --no-colors report coverage - raw.log - $confidential --copyright "Altinity Inc." --logo ./altinity.png | tfs --debug --no-colors document convert > coverage.html
tfs --debug --no-colors report results -a "https://$artifact_s3_bucket_path.s3.amazonaws.com/index.html#$artifact_s3_dir/" raw.log - $confidential --copyright "Altinity Inc." --logo ./altinity.png | tfs --debug --no-colors document convert > report.html
tfs --debug --no-colors report compare results --log compact.log --order-by version $confidential --copyright "Altinity Inc." --logo ./altinity.png | tfs --debug --no-colors document convert > compare.html

#Specify whether logs should be uploaded.
if [[ $1 == 1 ]];
then
    echo "::notice title=$SUITE$STORAGE $(uname -i) s3 logs and reports::https://$artifact_s3_bucket_path.s3.amazonaws.com/index.html#$artifact_s3_dir/$(uname -i)/$SUITE$STORAGE/"
    aws s3 cp pipeline_url.log.txt s3://$artifact_s3_bucket_path/$artifact_s3_dir/pipeline_url.log.txt --content-type "text/plain; charset=utf-8"
    aws s3 cp version.log.txt s3://$artifact_s3_bucket_path/$artifact_s3_dir/$(uname -i)/$SUITE$STORAGE/version.log.txt --content-type "text/plain; charset=utf-8"
    aws s3 cp raw.log s3://$artifact_s3_bucket_path/$artifact_s3_dir/$(uname -i)/$SUITE$STORAGE/raw.log
    aws s3 cp compact.log s3://$artifact_s3_bucket_path/$artifact_s3_dir/$(uname -i)/$SUITE$STORAGE/compact.log
    aws s3 cp nice.log.txt s3://$artifact_s3_bucket_path/$artifact_s3_dir/$(uname -i)/$SUITE$STORAGE/nice.log.txt --content-type "text/plain; charset=utf-8"
    aws s3 cp short.log.txt s3://$artifact_s3_bucket_path/$artifact_s3_dir/$(uname -i)/$SUITE$STORAGE/short.log.txt --content-type "text/plain; charset=utf-8"
    aws s3 cp report.html s3://$artifact_s3_bucket_path/$artifact_s3_dir/$(uname -i)/$SUITE$STORAGE/report.html
    aws s3 cp compare.html s3://$artifact_s3_bucket_path/$artifact_s3_dir/$(uname -i)/$SUITE$STORAGE/compare.html
    aws s3 cp coverage.html s3://$artifact_s3_bucket_path/$artifact_s3_dir/$(uname -i)/$SUITE$STORAGE/coverage.html
    sudo rm --recursive --force $SUITE/_instances/*/database/
    aws s3 cp . s3://$artifact_s3_bucket_path/$artifact_s3_dir/$(uname -i)/$SUITE$STORAGE/ --recursive --exclude "*" --include "*/_instances/*/logs/*.log" --content-type "text/plain; charset=utf-8"
    aws s3 cp . s3://$artifact_s3_bucket_path/$artifact_s3_dir/$(uname -i)/$SUITE$STORAGE/ --recursive --exclude "*" --include "*/_instances/*.log" --content-type "text/plain; charset=utf-8"
fi
