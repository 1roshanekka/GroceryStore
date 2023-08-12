import pyhtml as h

t = h.html(
        h.head(
            # login page
            h.title('Login')
        ),
        h.body(
            h.div(h.h1('Manager Login')),
            h.div(),
            h.div(h.h3('inside div')),
            h.p('Some paragraph')
        )
)

print(t.render())