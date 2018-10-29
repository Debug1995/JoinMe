from tkinter import *


def post_event():
    event_title = title_input.get()
    print(event_title)
    return


def update_event():
    event_title = title_input.get()
    print(event_title)
    return


def remove_user():
    print('remove')
    return


def register():
    return


def update_profile():
    return


def search_user():
    return


def update():
    return 


def group_email():
    return


def invite_friend():
    return


window = Tk()
window.title('JoinMe')
window.geometry('1000x650')
title = Label(window, text='JoinMe',)
title.config(font='Helvetica -20 bold', fg='black')
title.place(x=375, y=20, anchor="center")

# ------------------------------------------- Event -------------------------------------------

Event_title = Label(window, text='Title:')
Event_title.place(x=90, y=30)
title_input = Entry(window, relief='ridge', width=50)
title_input.place(x=170, y=30)

Event_Description = Label(window, text='Description:')
Event_Description.place(x=90, y=60)
Description_input = Entry(window, relief='ridge', width=50)
Description_input.place(x=170, y=60)

Event_Tags = Label(window, text='Tags:')
Event_Tags.place(x=90, y=90)
Tags_input = Entry(window, relief='ridge', width=50)
Tags_input.place(x=170, y=90)

Event_image = Label(window, text='Image URL:')
Event_image.place(x=90, y=120)
image_input = Entry(window, relief='ridge', width=50)
image_input.place(x=170, y=120)

Event_event_date = Label(window, text='Event Date:')
Event_event_date.place(x=90, y=150)
event_date_input = Entry(window, relief='ridge', width=50)
event_date_input.place(x=170, y=150)

Event_location = Label(window, text='Location:')
Event_location.place(x=90, y=180)
location_input = Entry(window, relief='ridge', width=50)
location_input.place(x=170, y=180)

Event_period = Label(window, text='Time Period:')
Event_period.place(x=90, y=210)
period_input = Entry(window, relief='ridge', width=50)
period_input.place(x=170, y=210)

post_button = Button(window, text="Post Event", command=post_event)
post_button.place(x=90, y=240)

update_button = Button(window, text="Update Event", command=update_event)
update_button.place(x=170, y=240)


Event_user = Label(window, text='User ID:')
Event_user.place(x=180, y=265)
userID_input = Entry(window, relief='ridge', width=10)
userID_input.place(x=240, y=270)

remove_button = Button(window, text="Remove User", command=remove_user)
remove_button.place(x=90, y=265)

label_user = Label(window,
                   text='------------------------------------------- User -------------------------------------------')
label_user.place(x=55, y=295)

# ------------------------------------------- User -------------------------------------------

User_Realname = Label(window, text='Real Name:')
User_Realname.place(x=90, y=315)
Realname_input = Entry(window, relief='ridge', width=50)
Realname_input.place(x=170, y=315)

User_Nickname = Label(window, text='Nickname:')
User_Nickname.place(x=90, y=345)
Nickname_input = Entry(window, relief='ridge', width=50)
Nickname_input.place(x=170, y=345)

User_Gender = Label(window, text='Gender:')
User_Gender.place(x=90, y=375)
Gender_input = Entry(window, relief='ridge', width=50)
Gender_input.place(x=170, y=375)

User_Location = Label(window, text='Location:')
User_Location.place(x=90, y=405)
Location_input = Entry(window, relief='ridge', width=50)
Location_input.place(x=170, y=405)

User_Email = Label(window, text='Email:')
User_Email.place(x=90, y=435)
Email_input = Entry(window, relief='ridge', width=50)
Email_input.place(x=170, y=435)

User_UserTags = Label(window, text='Tags:')
User_UserTags.place(x=90, y=465)
UserTags_input = Entry(window, relief='ridge', width=50)
UserTags_input.place(x=170, y=465)

User_Description = Label(window, text='Description:')
User_Description.place(x=90, y=495)
Description_input = Entry(window, relief='ridge', width=50)
Description_input.place(x=170, y=495)

register_button = Button(window, text="Register", command=register)
register_button.place(x=90, y=525)

updateProfile_button = Button(window, text="Update Profile", command=update_profile)
updateProfile_button.place(x=155, y=525)

User_userEmail = Label(window, text='User Email:')
User_userEmail.place(x=180, y=550)
userEmail_input = Entry(window, relief='ridge', width=10)
userEmail_input.place(x=260, y=550)

search_button = Button(window, text="Search User", command=search_user)
search_button.place(x=90, y=550)

# ------------------------------------------- Email -------------------------------------------

group_email_button = Button(window, text="Group Email", command=group_email)
group_email_button.place(x=90, y=580)

invite_friend_button = Button(window, text="Invite Friend", command=invite_friend)
invite_friend_button.place(x=180, y=580)

User_Nickname = Label(window, text='User Nickname:')
User_Nickname.place(x=270, y=580)
nickname_input = Entry(window, relief='ridge', width=10)
nickname_input.place(x=380, y=580)


# ------------------------------------------- Output -------------------------------------------

output = Label(window, text='Output')
output.place(x=800, y=20)
output_value = Label(window, text=update())
output_value.place(x=700, y=40)

window.mainloop()
