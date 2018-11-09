import gevent
import NGreenletProfiler

MILLION = 1000 * 1000

def foo():
    for i in range(20 * MILLION):
        if not i % MILLION:
            gevent.sleep(0)

def bar():
    for i in range(10 * MILLION):
        if not i % MILLION:
            gevent.sleep(0)

NGreenletProfiler.set_clock_type('cpu')
NGreenletProfiler.start()
foo_greenlet = gevent.spawn(foo)
bar_greenlet = gevent.spawn(bar)
foo_greenlet.join()
bar_greenlet.join()
NGreenletProfiler.stop()
stats = NGreenletProfiler.get_func_stats()
stats.save('NGreenletProfiler.callgrind', type='callgrind')
