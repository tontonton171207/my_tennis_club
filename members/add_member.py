from models import Member

member1 = Member(first_name='Tobias', last_name='Refsnes')
member2 = Member(first_name='Linus', last_name='Refsnes')
member3 = Member(first_name='Lene', last_name='Refsnes')
member4 = Member(first_name='Stale', last_name='Refsnes')
member5 = Member(first_name='Jane', last_name='Doe')
members_list = [member1, member2, member3, member4, member5]
for x in members_list:
    x.save()

Member.objects.all().values()