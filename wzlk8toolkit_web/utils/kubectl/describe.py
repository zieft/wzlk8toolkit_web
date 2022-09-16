from utils.kubectl.base import KubelctlExecutor


class KubectlDescribe(KubelctlExecutor):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.primary_com = ['kubectl', 'describe']

    def pods(self):
        self.args = ['pods']
        self.generate_command()
        self.excutecommand()

