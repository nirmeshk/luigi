wget -q -O - http://pkg.jenkins-ci.org/debian/jenkins-ci.org.key | apt-key add -
echo deb http://pkg.jenkins-ci.org/debian binary/ > /etc/apt/sources.list.d/jenkins.list
apt-get update
apt-get upgrade -f -y

apt-get install -y python-pbs
apt-get install -y sendmail

apt-get install -y jenkins
apt-get install -y git
/etc/init.d/jenkins start
