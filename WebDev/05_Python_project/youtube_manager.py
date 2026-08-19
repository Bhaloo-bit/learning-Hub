
import json

def load_data():
    try :
        with open('youtube.txt','r') as file:
            return json.load(file)
        
    except FileNotFoundError:
        return []

def save_data_helper(videos):
    with open('youtube.txt', 'w') as file:
        json.dump(videos, file)   

def list_all_videos(videos):
    print('\n')
    print("*" * 65)
    for index, video in enumerate(videos, start = 1):
        
        print(f"{index}. {video['name']}, Duration : {video['time']}")
    print('\n')
    print("*" * 65)
def add_video(videos):
    name = input("Enter video name: ")
    time = input("Enter video time: ")
    videos.append({'name': name, 'time':time})
    save_data_helper(videos)

def update_video(videos):
    list_all_videos(videos)
    index = int(input("enter the videos number to update"))
    if 1 <= index <= len(videos):
        name = input("Enter the video name")
        time = input("Enter the video time")
        videos[index-1] = {'name': name, 'time': time}
        save_data_helper(videos)
    else:
        print(" ! invalid index seleted")    

def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the vidoes number to be deleted"))

    if 1<= index <= len(videos):
        del videos[index-1]
        save_data_helper(videos)
    else:
        print("! invalid videos index seleted")    
def main():
    videos = load_data()
    while True:
        print("\n Youtube Manager | Choose an option ")
        print("1. list all youtube videos")
        print("2. Add a youtube videos")
        print("3. Update a youtube videos details")
        print("4. Delete a youtube videos")
        print("5. Exit the app")
        choice = input("Enter your choice: ")
        print(videos)

        if choice == '1':
            list_all_videos(videos)
        elif choice =='2':
            add_video(videos)
        elif choice == '3':
            update_video(videos)    
        elif choice == '4':
            delete_video(videos)
        elif choice == '5':
            break
        else:
            print("! invalid Choice")


if __name__ == '__main__':
    main()