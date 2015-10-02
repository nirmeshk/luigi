### Team
- Nirmesh Khandelwal (nbkhande@ncsu.edu)
- Xavier Primus (xjprimus@ncsu.edu)
- Trey Moore (dtmoore3@ncsu.edu)


### Build section


#### The ability to trigger a build in response to a git commit via a git hook.
- We achieved this using github webhooks. Once you finish setting up Jenkins server, we can trigger the build by url, using the “Trigger builds remotely” option in the “Build Triggers” section of job configuration. 
- ![Webhook](images/webhook.png)

#### The ability to execute a build job via a script or build manager (e.g., shell, maven), which ensures a clean build each time.:
- In Jenkins we have following commands to ensure clean build:
```shell
#!/bin/bash
echo ${GIT_BRANCH#*/}
rm -rf ../virtual_env/
virtualenv ../virtual_env
source ../virtual_env/bin/activate
python setup.py install
pip install tornado tox
tox -e py27-nonhdfs
```
- As you can see, every time a build is triggered, we create a fresh python virtualenv, install all the dependencies in clean environment and run all the unit test cases.

#### The ability to determine failure or success of a build job, and as a result trigger an external event (run post-build task, send email, etc).
- We have configured Jenkins to send the failure reports via email.
- ![Post build](post-build.png)
