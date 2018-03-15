#!/usr/bin/env python3.5

import drmaa
import os

def main():
    """Submit a job.
    Note, need file called sleeper.sh in home directory. An example:
    echo 'Hello World $*'
    """
    s = drmaa.Session()
    s.initialize()

    print('Creating job template')
    jt = s.createJobTemplate()
    jt.remoteCommand = os.getcwd() + '/sleeper.sh'
    jt.args = ['Simon says:', '42']
    jt.joinFiles = True

    # this puts the output in a file ~/tmp/DRMAA_JOB_OUT
    jt.outputPath = ":" + drmaa.JobTemplate.HOME_DIRECTORY + '/tmp/DRMAA_JOB_OUT'

    jobid = s.runJob(jt)
    print('Your job has been submitted with id ' + jobid)
    print(s.jobStatus(jobid))

    print('Cleaning up')
    s.deleteJobTemplate(jt)
    s.exit()

if __name__=='__main__':
    main()

