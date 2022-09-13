from django.forms import RadioSelect


class ColorRadioSelect(RadioSelect):
    """ Rebuild of RadioSelect class, using customised template. """

    template_name = 'widgets/color_radio/radio.html'
    option_template_name = 'widgets/color_radio/radio_option.html'
