import tkinter as tk
from tkinter import ttk, messagebox
import pyperclip

no_checkmark = '''<div dir="ltr" class="css-1rynq56 r-bcqeeo r-qvutc0 r-37j5jr r-a023e6 r-rjixqe r-16dba41 r-xoduu5 r-18u37iz r-1q142lx" style="text-overflow: unset; color: rgb(231, 233, 234)" > <span class="css-1qaijid r-bcqeeo r-qvutc0 r-poiln3 r-1awozwy r-xoduu5" style="text-overflow: unset" ></span> </div>'''

blue_checkmark = '''<span class="css-1qaijid r-bcqeeo r-qvutc0 r-poiln3 r-1pos5eu" style="text-overflow: unset;"><span class="css-1qaijid r-bcqeeo r-qvutc0 r-poiln3 r-adyw6z r-135wba7 r-xoduu5 r-18u37iz r-1q142lx" style="text-overflow: unset;"><span class="css-1qaijid r-bcqeeo r-qvutc0 r-poiln3 r-1awozwy r-xoduu5" style="text-overflow: unset;"><div class="css-175oi2r r-xoduu5"><div aria-label="Provides details about verified accounts." role="button" tabindex="0" class="css-175oi2r r-9cviqr r-6koalj r-1loqt21 r-o7ynqc r-6416eg r-1ny4l3l"><svg viewBox="0 0 22 22" aria-label="Verified account" role="img" class="r-4qtqp9 r-yyyyoo r-1xvli5t r-bnwqim r-1plcrui r-lrvibr r-1cvl2hr r-f9ja8p r-og9te1" data-testid="icon-verified"><g><path d="M20.396 11c-.018-.646-.215-1.275-.57-1.816-.354-.54-.852-.972-1.438-1.246.223-.607.27-1.264.14-1.897-.131-.634-.437-1.218-.882-1.687-.47-.445-1.053-.75-1.687-.882-.633-.13-1.29-.083-1.897.14-.273-.587-.704-1.086-1.245-1.44S11.647 1.62 11 1.604c-.646.017-1.273.213-1.813.568s-.969.854-1.24 1.44c-.608-.223-1.267-.272-1.902-.14-.635.13-1.22.436-1.69.882-.445.47-.749 1.055-.878 1.688-.13.633-.08 1.29.144 1.896-.587.274-1.087.705-1.443 1.245-.356.54-.555 1.17-.574 1.817.02.647.218 1.276.574 1.817.356.54.856.972 1.443 1.245-.224.606-.274 1.263-.144 1.896.13.634.433 1.218.877 1.688.47.443 1.054.747 1.687.878.633.132 1.29.084 1.897-.136.274.586.705 1.084 1.246 1.439.54.354 1.17.551 1.816.569.647-.016 1.276-.213 1.817-.567s.972-.854 1.245-1.44c.604.239 1.266.296 1.903.164.636-.132 1.22-.447 1.68-.907.46-.46.776-1.044.908-1.681s.075-1.299-.165-1.903c.586-.274 1.084-.705 1.439-1.246.354-.54.551-1.17.569-1.816zM9.662 14.85l-3.429-3.428 1.293-1.302 2.072 2.072 4.4-4.794 1.347 1.246z"></path></g></svg></div></div></span></span></span>'''

yellow_checkmark = '''<span class="css-1qaijid r-bcqeeo r-qvutc0 r-poiln3 r-1awozwy r-xoduu5" style="text-overflow: unset;"><div class="css-175oi2r r-xoduu5"><div aria-label="Provides details about verified accounts." role="button" tabindex="0" class="css-175oi2r r-9cviqr r-6koalj r-1loqt21 r-o7ynqc r-6416eg r-1ny4l3l"><svg viewBox="0 0 22 22" aria-label="Verified account" role="img" class="r-4qtqp9 r-yyyyoo r-1xvli5t r-bnwqim r-1plcrui r-lrvibr r-f9ja8p r-og9te1" data-testid="icon-verified"><g><linearGradient gradientUnits="userSpaceOnUse" id="1-a" x1="4.411" x2="18.083" y1="2.495" y2="21.508"><stop offset="0" stop-color="#f4e72a"></stop><stop offset=".539" stop-color="#cd8105"></stop><stop offset=".68" stop-color="#cb7b00"></stop><stop offset="1" stop-color="#f4ec26"></stop><stop offset="1" stop-color="#f4e72a"></stop></linearGradient><linearGradient gradientUnits="userSpaceOnUse" id="1-b" x1="5.355" x2="16.361" y1="3.395" y2="19.133"><stop offset="0" stop-color="#f9e87f"></stop><stop offset=".406" stop-color="#e2b719"></stop><stop offset=".989" stop-color="#e2b719"></stop></linearGradient><g clip-rule="evenodd" fill-rule="evenodd"><path d="M13.324 3.848L11 1.6 8.676 3.848l-3.201-.453-.559 3.184L2.06 8.095 3.48 11l-1.42 2.904 2.856 1.516.559 3.184 3.201-.452L11 20.4l2.324-2.248 3.201.452.559-3.184 2.856-1.516L18.52 11l1.42-2.905-2.856-1.516-.559-3.184zm-7.09 7.575l3.428 3.428 5.683-6.206-1.347-1.247-4.4 4.795-2.072-2.072z" fill="url(#1-a)"></path><path d="M13.101 4.533L11 2.5 8.899 4.533l-2.895-.41-.505 2.88-2.583 1.37L4.2 11l-1.284 2.627 2.583 1.37.505 2.88 2.895-.41L11 19.5l2.101-2.033 2.895.41.505-2.88 2.583-1.37L17.8 11l1.284-2.627-2.583-1.37-.505-2.88zm-6.868 6.89l3.429 3.428 5.683-6.206-1.347-1.247-4.4 4.795-2.072-2.072z" fill="url(#1-b)"></path><path d="M6.233 11.423l3.429 3.428 5.65-6.17.038-.033-.005 1.398-5.683 6.206-3.429-3.429-.003-1.405.005.003z" fill="#d18800"></path></g></g></svg></div></div></span>'''

def make_html(profile_name, username, profile_image_url, unread_items, checkmark):
    if checkmark == "No checkmark":
        checkmark = no_checkmark
    elif checkmark == "Blue checkmark":
        checkmark = blue_checkmark
    elif checkmark == "Yellow checkmark":
        checkmark = yellow_checkmark
    
    finalHTML = f'''<div aria-label="made by @clopso" role="button" tabindex="0" class="css-175oi2r r-ymttw5 r-1f1sjgu r-1loqt21 r-o7ynqc r-6416eg r-1ny4l3l"> <div class="css-175oi2r r-18u37iz"> <div class="css-175oi2r r-18kxxzh r-1kb76zh r-onrtq4 r-1777fci"> <div class="css-175oi2r r-bztko3 r-1adg3ll r-13qz1uu" data-testid="UserAvatar-Container" style="height: 40px" > <div class="r-1adg3ll r-13qz1uu" style="padding-bottom: 100%"></div> <div class="r-1p0dtai r-1pi2tsx r-u8s1d r-1d2f490 r-ipm5af r-13qz1uu"> <div class="css-175oi2r r-1adg3ll r-1pi2tsx r-13qz1uu r-u8s1d r-1wyvozj r-1v2oles r-desppf r-bztko3" > <div class="r-1p0dtai r-1pi2tsx r-u8s1d r-1d2f490 r-ipm5af r-13qz1uu" > <div class="css-175oi2r r-sdzlij r-1udh08x r-u8s1d r-ggadg3 r-8jfcpp" style="width: calc(100% + 4px); height: calc(100% + 4px)" > <div aria-hidden="true" role="presentation" tabindex="-1" class="css-175oi2r r-1pi2tsx r-13qz1uu r-1ny4l3l" style="background-color: rgba(0, 0, 0, 0)" > <div class="css-175oi2r r-sdzlij r-1udh08x r-633pao r-u8s1d r-1wyvozj r-1v2oles r-desppf" style="width: calc(100% - 4px); height: calc(100% - 4px)" > <div class="css-175oi2r r-1pi2tsx r-13qz1uu" style="background-color: rgba(0, 0, 0, 0)" ></div> </div> <div class="css-175oi2r r-sdzlij r-1udh08x r-633pao r-u8s1d r-1wyvozj r-1v2oles r-desppf" style="width: calc(100% - 4px); height: calc(100% - 4px)" > <div class="css-175oi2r r-1pi2tsx r-13qz1uu r-kemksi"></div> </div> <div class="css-175oi2r r-sdzlij r-1udh08x r-633pao r-u8s1d r-1wyvozj r-1v2oles r-desppf" style=" background-color: rgb(0, 0, 0); width: calc(100% - 4px); height: calc(100% - 4px); " > <div class="css-175oi2r r-1adg3ll r-1udh08x" style=""> <div class="r-1adg3ll r-13qz1uu" style="padding-bottom: 100%" ></div> <div class="r-1p0dtai r-1pi2tsx r-u8s1d r-1d2f490 r-ipm5af r-13qz1uu" > <div aria-label="" class="css-175oi2r r-1mlwlqe r-1udh08x r-417010" style="position: absolute; inset: 0px" > <div class="css-175oi2r r-1niwhzg r-vvn4in r-u6sd8q r-1p0dtai r-1pi2tsx r-1d2f490 r-u8s1d r-zchlnj r-ipm5af r-13qz1uu r-1wyyakw r-4gszlv" style=" background-image: url('{profile_image_url}'); " ></div> </div> </div> </div> </div> </div> </div> </div> </div> </div> </div> </div> <div class="css-175oi2r r-1iusvr4 r-16y2uox r-1777fci"> <div class="css-175oi2r r-1awozwy r-18u37iz r-1wtj0ep"> <div class="css-175oi2r r-1wbh5a2 r-dnmrzs r-1ny4l3l"> <div class="css-175oi2r r-1wbh5a2 r-dnmrzs r-1ny4l3l"> <div class="css-175oi2r r-1wbh5a2 r-dnmrzs r-1ny4l3l"> <div class="css-175oi2r r-1awozwy r-18u37iz r-dnmrzs"> <div dir="ltr" class="css-1rynq56 r-bcqeeo r-qvutc0 r-37j5jr r-a023e6 r-rjixqe r-b88u0q r-1awozwy r-6koalj r-1udh08x r-3s2u2q" style="text-overflow: unset; color: rgb(231, 233, 234)" > <div dir="ltr" class="css-1rynq56 r-bcqeeo r-qvutc0 r-37j5jr r-a023e6 r-rjixqe r-b88u0q r-1awozwy r-6koalj r-1udh08x r-3s2u2q" style="text-overflow: unset; color: rgb(231, 233, 234)" > <span class="css-1qaijid r-dnmrzs r-1udh08x r-3s2u2q r-bcqeeo r-qvutc0 r-poiln3" style="text-overflow: unset" ><span class="css-1qaijid r-bcqeeo r-qvutc0 r-poiln3" style="text-overflow: unset" >{profile_name}</span ><span class="css-1qaijid r-bcqeeo r-qvutc0 r-poiln3 r-1pos5eu" style="text-overflow: unset" ></span ></span> </div> </div> {checkmark} </div> </div> <div class="css-175oi2r r-1awozwy r-18u37iz r-1wbh5a2"> <div tabindex="-1" class="css-175oi2r r-1wbh5a2 r-dnmrzs r-1ny4l3l" > <div class="css-175oi2r"> <div dir="ltr" class="css-1rynq56 r-dnmrzs r-1udh08x r-3s2u2q r-bcqeeo r-qvutc0 r-37j5jr r-a023e6 r-rjixqe r-16dba41 r-18u37iz r-1wvb978" style="text-overflow: unset; color: rgb(113, 118, 123)" > <span class="css-1qaijid r-bcqeeo r-qvutc0 r-poiln3" style="text-overflow: unset" >{username}</span > </div> </div> </div> </div> </div> </div> <div dir="ltr" aria-label="{unread_items} unread items" aria-live="polite" class="css-1rynq56 r-qvutc0 r-37j5jr r-1b43r93 r-1cwl3u0 r-b88u0q r-1awozwy r-l5o3uw r-sdzlij r-6koalj r-1q142lx r-1777fci r-lrvibr r-3s2u2q r-1xc7w19 r-1phboty r-rs99b7 r-1tjplnt r-z80fyv r-i61hcz r-19u6a5r" style="text-overflow: unset; color: rgb(255, 255, 255)" > <span class="css-1qaijid r-bcqeeo r-qvutc0 r-poiln3" style="text-overflow: unset" >{unread_items}</span > </div> </div> </div> </div></div>'''
    
    return finalHTML


class TwitterGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Twitter Profile Cloner")

        # Set window size
        self.root.geometry("350x350")

        # Keep window on top
        self.root.attributes("-topmost", True)

        # Profile Name entry
        self.profile_name_label = ttk.Label(root, text="Profile Name:")
        self.profile_name_label.pack()
        self.profile_name_entry = ttk.Entry(root, width=20)
        self.profile_name_entry.pack(pady=5)

        # Username entry
        self.username_label = ttk.Label(root, text="Username:")
        self.username_label.pack()
        self.username_entry = ttk.Entry(root, width=20)
        self.username_entry.insert(0, "@")
        self.username_entry.pack(pady=5)

        # Profile Image URL entry
        self.profile_image_label = ttk.Label(root, text="Profile Image URL:")
        self.profile_image_label.pack()
        self.profile_image_entry = ttk.Entry(root, width=40)
        self.profile_image_entry.pack(pady=5)
        
        # Unread Items entry
        self.unread_items_label = ttk.Label(root, text="Unread Items (Number):")
        self.unread_items_label.pack()
        self.unread_items_entry = ttk.Entry(root, width=10, justify="center")  # Adjust width here
        self.unread_items_entry.pack(pady=5)
        
        # Checkmark dropdown
        self.checkmark_label = ttk.Label(root, text="Select Checkmark:")
        self.checkmark_label.pack()
        self.checkmark_options = ttk.Combobox(root, values=["No checkmark", "Blue checkmark", "Yellow checkmark"])
        self.checkmark_options.pack(pady=5)
        self.checkmark_options.current(0)  # Set default value to "No checkmark"

        # Submit Button
        self.submit_button = ttk.Button(root, text="Submit", command=self.submit)
        self.submit_button.pack(pady=20)

    def submit(self):
        profile_name = self.profile_name_entry.get()
        username = self.username_entry.get()
        profile_image_url = self.profile_image_entry.get()
        unread_items = self.unread_items_entry.get()
        checkmark = self.checkmark_options.get()

        # Combine text
        message = f"Profile Name: {profile_name}\nUsername: {username}\nProfile Image URL: {profile_image_url}\nTwitter Profile URL: {profile_image_url}\nCheckmark: {checkmark}"

        # Copy text to clipboard
        pyperclip.copy(make_html(profile_name, username, profile_image_url, unread_items, checkmark))

        # Show message box
        messagebox.showinfo("Success!", "HTML copied to clipboard with this info:\n\n" + message)

if __name__ == "__main__":
    root = tk.Tk()
    app = TwitterGUI(root)
    root.mainloop()
