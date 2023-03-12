from clients import TeachableAPIClient

'''
[Course(id=2002430, name='Trees and Arboreous Concerns', heading='Grow Your Knowledge of Trees and Arboreous Concerns - Learn From the Expert!', description=None, is_published=True, image_url='https://cdn.filestackcontent.com/HfhcrI
RZKEyvND8blEXA'), Course(id=2002431, name='Mushroom Madness', heading='Unlock the Secrets of Mushroom Foraging with Mushroom Madness', description=None, is_published=True, image_url='https://cdn.filestackcontent.com/MKdUddC0R9iLDP27
yF1L'), Course(id=2002436, name='Herbal Teas & Other Garden Tinctures', heading='Brew your own natural remedies with Herbal Teas &amp; Other Garden Tinctures', description=None, is_published=True, image_url='https://cdn.filestackcon
tent.com/4PhkBhwMS0q1e4yCkoVO')]
'''

def test_client():
    client = TeachableAPIClient()
    users = {}
    courses = {}
    enrollments = {}

    for user in client.list_users():
        users[user.id] = user

    for course in client.list_published_courses():
        courses[course.id] = course
        enrollments[course.id] = []
        for enrollment in client.list_enrollments(course_id=course.id):
            enrollments[course.id].append(enrollment)

    import ipdb; ipdb.set_trace()



if __name__ == "__main__":
   test_client()
