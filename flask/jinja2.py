# jinja2
pip install jinja2

from jinja2 import Template

#기본구조
#1. html을 내부.py에서 작성했을시
template_str = """
<h1>{{ title }}</h1>
<p>{{ description }}</p>
"""
a = Template(template_str)   #먼저 Template으로 감싸

data = {                        #값들 딕셔너리형태로
    "title": "Welcome to Jinja2",
    "description": "This is a simple Jinja2 example."
}

# 렌더링: 템플릿에 데이터를 삽입하여 최종 HTML 생성
result = a.render(data)
print(result)   #-> {{title}}, {{description}}에 data 값들 들어간 형태


#2. 외부 html가져오기
# hello.html이 templates디렉토리에 존재

from jinja2 import Environment, FileSystemLoader

# 템플릿 파일이 있는 디렉토리 경로을 인자로 전달하여 Environment 객체 생성
env = Environment(loader=FileSystemLoader('templates'))   #templates디렉토리로 이동

# Environment 객체로 부터 템플릿 로딩
a = env.get_template('hello.html')   #디렉토리안의 hello.html가져와 template으로 감쌈

# 데이터
data = {'name': 'Jinja2'}

# 렌더링: 템플릿에 데이터를 삽입하여 최종 HTML 생성
rendered_html = a.render(data)  #data딕셔너리 이용해 렌더

print(rendered_html)   #원하는 data들어 html구조 가져옴


# 3. 데이터의 딕셔너리안의 딕셔너리
data = {
    "user": {
        "name": "John",
        "age": 30
    }
}

template_str = "{{ user.name }} is {{ user.age }} years old."    #a.b로 가져오기 가
template = Template(template_str)
result = template.render(data)
print(result)  # 출력: John is 30 years old.


#4. 변수연산 가능
data = {
    "variable": 10
}

template_str = "{{ variable + 1 }}"
template = Template(template_str)
result = template.render(data)
print(result)  # 출력: 11



#5. if문    조건증 히니민 실
template_str = """
{% if user.age >= 18 %}
    <p>{{ user.name }} is an adult.</p>
{% else %}
    <p>{{ user.name }} is a minor.</p>
{% endif %}
"""

template = Template(template_str)

data = {
    "user": {
        "name": "John",
        "age": 30
    }
}

result = template.render(data)
print(result)


#6. for문
template_str = """
<ul>
{% for item in items %}
    <li>{{ item }}</li>
{% endfor %}
</ul>
"""

template = Template(template_str)

data = {
    "items": ["Apple", "Banana", "Cherry"]
}

result = template.render(data)
print(result)


#7-1. macro
template_str = """
{% macro input(name, value='', type='text') %}
    <input type="{{ type }}" name="{{ name }}" value="{{ value }}">
{% endmacro %}

{{
    input('username')
}}
{{
    input('password', type='password')
}}
"""

template = Template(template_str)
result = template.render()
print(result)

#7-2. 다른 파일의 macro가져오기
#a.html - 'templates' 디렉토리에 저장:
{% macro input(name, value='', type='text') %}
    <input type="{{ type }}" name="{{ name }}" value="{{ value }}">
{% endmacro %'}'

#b.html - 'templates' 디렉토리에 저장:
{% from 'b.html' import input %}

{{
    input('username')
}}
{{
    input('password', type='password')
}}

#b.py 파이썬에
from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('macro_test.html')

result = template.render()
print(result)

