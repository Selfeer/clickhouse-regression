# Configuration of SSL-FIPS

## Prerequisites for FIPS-Compatible Operation
The minimal requirements for FIPS-compatible operation are: 

Install FIPS-compatible Altinity Stable build. 
Apply FIPS-compatible configuration settings to set allowed ports, TLS version, and ciphers. 

## FIPS-compatible configuration settings

## ClickHouse Server Configuration

Required server configuration changes including the following. These settings are by convention stored in /etc/clickhouse-server/config.xml /etc/clickhouse-server/config.d/. 
Disable all ports not in the FIPS-Compatible Network Protocol list, including the following. Comment them out and ensure they are not present in preprocessed_config.xml. 
* ClickHouse HTTP port
* ClickHouse TCP port
* Interserver http port
* Additional non-FIPS client protocols: MySQL, PostgreSQL, gRPC, etc. 

To properly configure ClickHouse with the SSL-FIPS settings, follow these instructions:

Place the configuration changes in the file /etc/clickhouse-server/config.d/fips.xml. This will ensure that your settings are not overridden when installing new Altinity Stable builds. Here is an example of the file contents:

```xml
<clickhouse>
	<https_port>8443</https_port>
	<tcp_port_secure>9440</tcp_port_secure>
	<interserver_https_port>9010</interserver_https_port>

	<openSSL>
    	<server>
        	<certificateFile>/etc/clickhouse-server/config.d/server.crt</certificateFile>
        	<privateKeyFile>/etc/clickhouse-server/config.d/server.key</privateKeyFile>
        	<dhParamsFile>/etc/clickhouse-server/config.d/dhparam.pem</dhParamsFile>
        	<verificationMode>none</verificationMode>
        	<loadDefaultCAFile>True</loadDefaultCAFile>
        	<cipherList>ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:AES128-GCM-SHA256:AES256-GCM-SHA384</cipherList>
        	<requireTLSv1_2>true</requireTLSv1_2>
        	<disableProtocols>sslv2,sslv3,tlsv1,tlsv1_1,tlsv1_3</disableProtocols>
        	<cacheSessions>true</cacheSessions>
        	<disableProtocols>sslv2,sslv3</disableProtocols>
        	<preferServerCiphers>true</preferServerCiphers>
    	</server>
    	<client>
        	<certificateFile>/etc/clickhouse-server/config.d/server.crt</certificateFile>
        	<privateKeyFile>/etc/clickhouse-server/config.d/server.key</privateKeyFile>
        	<loadDefaultCAFile>True</loadDefaultCAFile>
        	<cacheSessions>true</cacheSessions>
        	<requireTLSv1_2>true</requireTLSv1_2>
        	<disableProtocols>sslv2,sslv3,tlsv1,tlsv1_1,tlsv1_3</disableProtocols>
        	<preferServerCiphers>true</preferServerCiphers>
        	<verificationMode>none</verificationMode>
        	<invalidCertificateHandler>
            	<name>AcceptCertificateHandler</name>
        	</invalidCertificateHandler>
    	</client>
	</openSSL>
</clickhouse>
```

Note: There is no need to set openSSL/fips value to true in the XML above as it is enabled by default in the current build and cannot be turned off.
Also, make sure to replace ${CERT_PATH} and ${CA_PATH} placeholders with appropriate values for your configuration.

Create the file /etc/clickhouse-server/config.d/secure_keeper.xml and add your ClickHouse Keeper configuration there. Enable secure connection by adding <secure>1</secure> as shown in the example below for a 3-node Keeper cluster:

```xml
<clickhouse>
	<zookeeper>
    	<node>
        	<host>clickhouse1</host>
        	<port>9281</port>
        	<secure>1</secure>
    	</node>
    	<node>
        	<host>clickhouse2</host>
        	<port>9281</port>
        	<secure>1</secure>
    	</node>
    	<node>
        	<host>clickhouse3</host>
        	<port>9281</port>
        	<secure>1</secure>
    	</node>
	</zookeeper>
</clickhouse>
```


On the ClickHouse Keeper nodes, provide the ClickHouse Keeper configuration file in /etc/clickhouse-server/config.d/raft_keeper.xml. To enable ClickHouse Keeper secure connection, use <tcp_port_secure>9281</tcp_port_secure> setting in the keeper_server section and <secure>true</secure> setting in the raft_configuration section. Also <server_id> setting should be unique for every node.

```xml
<clickhouse>
	<keeper_server>
    	<tcp_port_secure>9281</tcp_port_secure>
    	<server_id>1</server_id>
    	<log_storage_path>/var/lib/clickhouse/coordination/log</log_storage_path>
    	<snapshot_storage_path>/var/lib/clickhouse/coordination/snapshots</snapshot_storage_path>

    	<coordination_settings>
        	<operation_timeout_ms>10000</operation_timeout_ms>
        	<session_timeout_ms>30000</session_timeout_ms>
        	<raft_logs_level>trace</raft_logs_level>
    	</coordination_settings>

    	<raft_configuration>
        	<secure>true</secure>
        	<server>
            	<id>1</id>
            	<hostname>clickhouse1</hostname>
            	<port>9444</port>
            	<secure>1</secure>
        	</server>
        	<server>
            	<id>2</id>
            	<hostname>clickhouse2</hostname>
            	<port>9444</port>
            	<secure>1</secure>

        	</server>
        	<server>
            	<id>3</id>
            	<hostname>clickhouse3</hostname>
            	<port>9444</port>
            	<secure>1</secure>
        	</server>
    	</raft_configuration>
	</keeper_server>
</clickhouse>
```

Define macros values on all nodes to be able to create a ReplicatedMergeTree table for testing.
```xml
<clickhouse>
	<macros>
    	<replica>clickhouse1</replica>
    	<shard>01</shard>
	</macros>
</clickhouse>
```

Finally, provide your cluster schema in the file /etc/clickhouse-server/config.d/remote.xml and add the tcp_port_secure as the port. Enable secure connection by adding <secure>1</secure>.

```xml
<clickhouse>
	<remote_servers>
    	<simple_replication_cluster>
        	<shard>
            	<replica>
                	<host>clickhouse1</host>
                	<port>9440</port>
                	<secure>1</secure>
            	</replica>
            	<replica>
                	<host>clickhouse2</host>
                	<port>9440</port>
                	<secure>1</secure>
            	</replica>
            	<replica>
                	<host>clickhouse3</host>
                	<port>9440</port>
                	<secure>1</secure>
            	</replica>
        	</shard>
    	</simple_replication_cluster>
	</remote_servers>
</clickhouse>
```

## ClickHouse Client Configuration

Make the required changes in the clickhouse-client configuration files /etc/clickhouse-client/config.xml and /etc/clickhouse-client/config.d/.
Configure the openSSL section in the config.xml file to restrict TLS to TLSv1.2 and FIPS 140.2-approved ciphers. Copy the values for the changes from the server fips.xml file and place them in /etc/clickhouse-client/config.d/fips.xml
or directly into /etc/clickhouse-client/config.xml if you don’t have client config file.

```xml
<config>
	<secure>true</secure>
	<openSSL>
  	<client>
      	<verificationMode>none</verificationMode>
      	<invalidCertificateHandler>
          	<name>AcceptCertificateHandler</name>
      	</invalidCertificateHandler>
      	<preferServerCiphers>true</preferServerCiphers>
      	<requireTLSv1_2>true</requireTLSv1_2>
      	<disableProtocols>sslv2,sslv3,tlsv1,tlsv1_1,tlsv1_3</disableProtocols>
      	<cipherList>ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:AES128-GCM-SHA256:AES256-GCM-SHA384</cipherList>
  	</client>
	</openSSL>
</config>
```

With these instructions, you should be able to properly configure ClickHouse and ClickHouse Client with the SSL_FIPS settings.

## Verification of FIPS-Compatible Altinity Stable Operation

### Verify SSL ports connection

```bash
$ openssl s_client -connect clickhouse1:9440
$ openssl s_client -connect clickhouse1:9281
$ openssl s_client -connect clickhouse1:9010
$ openssl s_client -connect clickhouse1:9444 ???
```

### Verify FIPS library Startup

On startup FIPS-compatible Altinity.Cloud servers will print the following message after a successful start-up test. This ensures that FIPS BoringSSL libraries are present and free from tampering. 

```bash
$ grep 'FIPS mode' /var/log/clickhouse-server/clickhouse-server.log
2023.05.28 18:19:03.064038 [ 1 ] {} <Information> Application: Starting in FIPS mode, KAT test result: 1
```
### Verify FIPS-Compatible Altinity Stable Version

To verify the software version, run ‘select version()’ on the running server with any client program. This example confirms the version for both clickhouse-client as well as clickhouse-server. 

```bash
$ clickhouse-client <options>
ClickHouse client version 22.8.15.25.altinityfips (altinity build).


5f1b329b5fdf :) select version()

SELECT version()

┌─version()───────────────┐
│ 22.8.15.25.altinityfips │
```