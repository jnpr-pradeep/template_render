import os
import json


CWD = os.getcwd()
OUTPUT_FILE = "output.txt"
TEMPLATE_FILE_NAME = "juniper_underlay_ip_clos.j2"
# TEMPLATE_FILE_NAME = "juniper_junos-qfx_underlay_infra_bms_access.j2"
INPUT_DATA = "values.json"


def get_input_data():
    with open(CWD + "/" + INPUT_DATA, 'r') as input_file:
        data = json.load(input_file)
    return data


def render_jinja_template():
    from jinja2 import Environment, FileSystemLoader, ext

    # Capture our current directory
    j2_env = Environment(loader=FileSystemLoader(CWD),
                         trim_blocks=True,
                         extensions=(ext.loopcontrols, ext.do))

    data = get_input_data()
    # print data
    print data['device_abstract_config']['physical_interfaces']
    render_resp = j2_env.get_template(TEMPLATE_FILE_NAME).render(**data)
    with open(OUTPUT_FILE, 'w') as h:
        h.write(render_resp)


render_jinja_template()
