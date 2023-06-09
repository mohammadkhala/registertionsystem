def student_completed_prerequisites(course, student_id):
    if not courses.prerequisites:
        return True

    completed_courses = db((db.registration.courses == db.courses.id) &
                            (db.registration.student == student_id) &
                            (db.registration.status == 'completed')).select(db.courses.ALL)
    completed_course_ids = [c.id for c in completed_courses]

    for prereq in course.prerequisites:
        if prereq not in completed_course_ids:
            return False

    return True

def add_course_to_schedule():
    student_id = request.vars.student_id
    course_id = request.vars.course_id

    course = db.courses(course_id)
    if not course:
        return 'Invalid course ID'

    if not student_completed_prerequisites(course, student_id):
        return 'Prerequisites not completed'

    if db(db.registration.student == student_id and db.registration.courses == course_id).count():
        return 'Course already registered'

    db.registration.insert(student=student_id, course=course_id)

    redirect(URL('default', 'index'))

def display_course_schedule():
    student_id = request.vars.studentid

    courses = db((db.courses.code == db.courses) &
                 (db.students.id == student_id)).select(db.courses.ALL)

    return dict(courses=courses)

def index():

    courses = db(db.courses).select()


    student_id = request.vars.studentid

    form = SQLFORM.factory(
        Field('courseid', 'integer', label='Course ID'),
        Field('studentid', 'integer', default=student_id, readable=False, writable=False),
        submit_button='Add Course',
    )

    if form.process().accepted:
        response.flash = add_course_to_schedule()

    course_schedule = display_course_schedule()

    return dict(form=form, courses_chedule=course_schedule,courses=courses)
