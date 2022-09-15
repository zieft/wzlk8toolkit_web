class BootstrapForm(object):
    bootstrap_class_exclude = []  # can be overrided by child.

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if name in self.bootstrap_class_exclude:
                continue
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = 'Please enter {}'.format(field.label)
