import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import io


def apply_frame(image, frame_path):
    # Open the image and the frame
    base_image = Image.open(image).convert("RGBA")
    frame = Image.open(frame_path).convert("RGBA")

    min_size = min(base_image.size)
    crop_box = ((base_image.width - min_size) // 2, (base_image.height - min_size) // 2,
                (base_image.width + min_size) // 2, (base_image.height + min_size) // 2)

    # Crop the base image to the maximum square size
    base_image = base_image.crop(crop_box)
    base_image = base_image.resize(frame.size)


    # Composite the image and the frame
    result = Image.alpha_composite(base_image, frame)

    return result


def main():
    st.title("Custom Profile For LOCUS 2024")
    st.text("Made with passion by Krishant Timilsina")

    # Upload image through Streamlit
    uploaded_file = st.file_uploader(
        "Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        st.image(uploaded_file, caption="Uploaded Image",
                 use_column_width=True)

        # Upload frame through Streamlit
        frame_file = 'frame.png'
        if st.button("Generate Result Image"):
        # Apply the frame on top of the image
            result_image = apply_frame(uploaded_file, frame_file)

            # Display the result image
            st.image(result_image, caption="Result Image",
                    use_column_width=True, channels="RGBA")
            result_image_path = "result_image.png"
            result_image.save(result_image_path)
            with open(result_image_path, "rb") as file:
                st.download_button(
                    label="Download image",
                    data=file,
                    file_name="result.png",
                    mime="image/png"
            )



if __name__ == "__main__":
    main()
