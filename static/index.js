const file_input = document.getElementById("file_input");
const preview = document.getElementById("preview");
const image = preview.querySelector(".image-preview__image");
const default_text = preview.querySelector(".image-preview__default-text");

file.addEventListener("change", function () {
  const file = this.file[0];
  console.log(file);

  if (file) {
    const reader = new FileReader();

    default_text.style.display = "none";
    image.style.display = "block";

    reader.addEventListener("load", function () {
      image.setAttribute("src", this.result);
    });

    reader.readAsDataURL(file);
  } else {
    default_text.style.display = null;
    image.style.display = null;
    image.setAttribute("src", "");
  }
});
