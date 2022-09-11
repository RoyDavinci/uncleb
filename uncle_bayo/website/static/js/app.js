const containerDiv = document.querySelector(".item_container");
const openDiv = document.querySelector(".fa-bars");
const closeDiv = document.querySelector(".fa-xmark");

openDiv.addEventListener("click", () => {
	if (containerDiv.classList.contains("hide")) {
		containerDiv.classList.remove("hide");
	}
});
closeDiv.addEventListener("click", () => {
	if (!containerDiv.classList.contains("hide")) {
		containerDiv.classList.add("hide");
	}
});
