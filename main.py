import re

txt = '''
<?xml version="1.0" encoding="utf-8" standalone="no"?>
<Context docBase="lims" >
	<Resource name="jdbc/lims" auth="Container" scope="Shareable" 
		factory="org.apache.tomcat.dbcp.dbcp2.BasicDataSourceFactory" 
		type="javax.sql.DataSource" 
		driverClassName="com.microsoft.sqlserver.jdbc.SQLServerDriver" 
		username="lims" password="lims" 
		maxTotal="100" 
		maxIdle="100" 
		maxWaitMillis="3000" 
		encrypt="false"
		url="jdbc:sqlserver://localhost:1433;DatabaseName=LIMSInnovaKurgan;applicationName=LIMS" 

	/>
</Context>
'''


reg1 = re.compile(r"DatabaseName=\w*")
sr = reg1.findall(txt)[0].replace('DatabaseName=', "")
