# import library
import cv2

# Function to load image
def load_image():
    path = input("Enter the path or name of the image: ")
    image = cv2.imread(path)
    if image is None:
        print(" Could not find the image. Please check the path.")
    else:
        print("Successfully loaded the image.")
    return image


# # Function to show image
# def show_image(image, win_name="Image"):
#     cv2.imshow(win_name, image)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
    



# Function to show image
def show_image(image, win_name="Image"):
    cv2.imshow(win_name, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
        
# function for image dimensions
def show_dimensions(image):
        h,w,c = image.shape
        print(f"Image loaded:\nheight: {h}\nwidth:{w}\nChannels:{c}")

    
# function for grayscale conversion
def convert_to_grayscale(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return gray

def resize_and_show(image):
    resized = cv2.resize(image,(300,300))
    cv2.imshow("Original Image.",image)
    cv2.imshow("Resized Image ",resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
def rotation(image):
    (h,w) = image.shape[:2]
    center = (w//2,h//2)
    M = cv2.getRotationMatrix2D(center,90,1.0)
    rotated = cv2.warpAffine(image,M,(w,h))
    cv2.imshow("Original Image",image)
    cv2.imshow("Rotated 90 degree image",rotated)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
def flip_image(image):
    flipped_horizontal = cv2.flip(image,1)
    flipped_vertical = cv2.flip(image,0)
    flipped_both = cv2.flip(image,-1)
    cv2.imshow("Original Image ",image)
    cv2.imshow("Flipped Horizontal Image",flipped_horizontal)
    cv2.imshow("Flipped vertical Image",flipped_vertical)
    cv2.imshow("Flipped Both Image",flipped_both)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
def Line_image(image):
    pt1 = (50,100)
    pt2 = (200,100)
    color = (0,0,255)
    thickness = 4
    cv2.line(image,pt1,pt2,color,thickness)
    cv2.imshow('line Drawing',image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
def Rect(image):
    pt1 = (50,50)
    pt2 = (250,200)
    color = (0,0,255) # pure red
    thickness = 3
    cv2.rectangle(image,pt1,pt2,color,thickness)
    cv2.imshow('Rectangle Drawing on Image',image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
def circle(image):
    center = (150,150)
    radius = 50
    color = (255,0,0)
    thickness = -1
    cv2.circle(image,center,radius,color,thickness)
    cv2.imshow('Drawing circle...',image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def text(image):
       cv2.putText(image,'Hello Python Programmers',(80,600),cv2.FONT_HERSHEY_SIMPLEX,1.2,
           (255,0,0),2)
       cv2.imshow('Adding text over image..',image)
       cv2.waitKey(0)
       cv2.destroyAllWindows()
    
# Main function
def main():
    image = None

    while True:
        print("\n Menu:")
        print("A - Load Image")
        print("B - Show Image")
        print("C - Show Dimensions")
        print("D - Show Grayscale Image")
        print("E - Resize image ")
        print("F - Rotating the image")
        print("G - Drawing Line on Image")
        print("H - Drawing Rectangle on Image")
        print("I - Drawing Circle on Image")
        print("J - Writing text on Image")
        print("Q - Quit")

        choice = input(" Enter your choice: ").upper()

        if choice == 'A':
            image = load_image()

        elif choice == 'B':
            if image is not None:
                show_image(image)
            else:
                print(" Please load an image first!")

        elif choice == 'C':
            if image is not None:
                show_dimensions(image)
            else:
                print(" Please load an image first!")

        elif choice == 'D':
            if image is not None:
                gray = convert_to_grayscale(image)
                show_image(gray, "Grayscale Image")
            else:
                print(" Please load an image first!")
                
        elif choice =='E':
            if image is not None:
                resize_and_show(image)
            else:
                print("could not Load the image")

        elif choice =='F':
            if image is not None:
                rotation(image)
            else:
                print("could not Load the image")
        
        elif choice =='F':
            if image is not None:
                flip_image(image)
            else:
                print("could not Load the image")
                
        elif choice =='G':
            if image is not None:
               Line_image(image)
            else:
                print("could not Load the image")
                
        elif choice =='H':
            if image is not None:
                Rect(image)
            else:
                print("could not Load the image")
                
        elif choice =='I':
            if image is not None:
                circle(image)
            else:
                print("could not Load the image")
                
        elif choice =='J':
            if image is not None:
                text(image)
            else:
                print("could not Load the image")           
        elif choice == 'Q':
            print(" Exiting...")
            break

        else:
            print(" Invalid choice! Try again.")

if __name__ == "__main__":
    main()
