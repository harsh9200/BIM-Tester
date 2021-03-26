import re

def remove_spaces(text) -> str:
    return ' '.join(text.split())


def remove_arrows(text) -> str:
    return text.replace('-->', '')


def insert_html(text, req=False) -> str:
    text = text.replace("'", '')
    for s in re.findall('"([^"]*)"', text):
        if not req:
            text = text.replace(
                s, f'<code contenteditable>{s}</code>')
        else:
            text = text.replace(s, '{}')
    return text


def create_requirements(Format, args):
    idx = 1
    text = 'Feature: Project setup\n\n'
    Headings = Format.get_headings(req=True)
    for intro in Format.get_intro():
        text += f'{intro}\n'
    text += '\n'

    while True:
        scenario = args.get(f'Scen_{str(idx)}')
        idx_inside = 1
        if scenario:
            text += f'{scenario}\n'
        while True:
            _input = args.get(f'Input_{str(idx)}_{str(idx_inside)}')

            headings = Headings[idx+idx_inside-2].format(_input)
            switch = args.get(f'Switch_{str(idx)}_{str(idx_inside)}')
            if switch:
                text += f'\t* {headings}\n'
            idx_inside += 1

            if _input is None:
                break

        text += '\n'
        idx += 1
        if not scenario:
            break
    print(text)

    file = open('features/project_setup.feature', 'w')
    file.write(text)
    file.close()
