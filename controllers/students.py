@auth.requires_login()

def addstudent():
    form = SQLFORM(db.students)
    if form.process().accepted:
        response.flash = 'form accepted'
    elif form.errors:
        response.flash = 'form has errors'
    else:
        response.flash = 'please fill out the form'

    return dict(form=form)


def students():

    grid = SQLFORM.grid(db.students)

    return dict(grid=grid)