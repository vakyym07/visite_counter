from bottle import route, run, app, request, response, redirect, get, post, template
from beaker.middleware import SessionMiddleware
from time import time
from datetime import datetime
import xml_handler as xh
from html_filter import filter_html


session_opts = {
    'session.type': 'memory',
    'session.save_accessed_time': True,
    'session.auto': True,
    'session.timeout': 1800
}

app = SessionMiddleware(app(), session_opts)
mlsecond_in_day = 86400000


def get_current_time():
    return int(round(time() * 1000))


@route('/counter')
def run_session():
    today = int(request.cookies.get('current_date', default='0'))
    if get_current_time() - today >= mlsecond_in_day:
        response.set_cookie('current_date', str(get_current_time()))
        response.set_cookie('today_visit', str(0))

    v_all = int(request.cookies.get('total_visit', default='0'))
    v_today = int(request.cookies.get('today_visit', default='0'))
    session = request.environ.get('beaker.session')
    client_ip = request.environ.get('REMOTE_ADDR')

    if session.get('client_ip') is None:
        session['client_ip'] = client_ip
        v_all += 1
        v_today += 1
        response.set_cookie('total_visit', str(v_all))
        response.set_cookie('today_visit', str(v_today))
    return '''
        <div>You visited this page {} times for all time</div>
        <div>You visited this page {} times for today</div>
        <div> Last visit in {}</div>
        '''.format(v_all, v_today, datetime.now().isoformat())


@get('/review')
def review():
    info = xh.get_all_reviews()
    info['title'] = 'Reviews'
    return template('reviews.tpl', info)


@post('/review')
def do_review():
    name = request.forms.get('name')
    a_review = request.forms.get('review')
    root = xh.get_root()
    xh.add_review_to_root(root, name, filter_html(a_review))
    xh.write(root)
    redirect('/review')


run(
    app=app,
    host='localhost',
    port=5000,
)
