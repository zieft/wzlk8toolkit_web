import subprocess


class KubelctlExecutor:
    def __init__(self, request):
        self.request = request
        self.task_name = request.tracer.project.name
        self.S3_bucket = request.tracer.project.bucket
        self.S3_key = request.tracer.project.S3_key
        self.S3_secret_key = request.tracer.project.S3_secret_key
        self.name_space = ['-n', request.tracer.project.name_space]

        self.command = []

        self.primary_com = None
        self.args = None

        self.stdout = None
        self.stdin = None
        self.stderr = None

    def excutecommand(self):
        ex = subprocess.Popen(self.command, stdout=subprocess.PIPE, shell=False)
        out, err = ex.communicate()
        status = ex.wait()
        if err:
            self.stderr = err.decode()
            return err.decode()

        if out:
            self.stdout = out.decode()
            return out.decode()

    def generate_command(self):
        self.command.extend(self.primary_com)
        self.command.extend(self.name_space)
        self.command.extend(self.args)

        print(self.command)


class KubectlDescribe(KubelctlExecutor):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.primary_com = ['kubectl', 'describe']

    def pods(self):
        self.args = ['pods']
        self.generate_command()
        self.excutecommand()


class KubectlApply(KubelctlExecutor):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.primary_com = ['kubectl', 'apply']

    def file(self):
        # check file existence again.
        self.args = ['-f', self.request.tracer.project.yaml]
        self.generate_command()
        self.excutecommand()
