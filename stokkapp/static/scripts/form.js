const makeItNew = document.querySelector(".makeItNew")

document.querySelector(".item_form").addEventListener("click", (evt) => {
    if (evt.target.dispatchEvent.startswith("new_item")) {
        makeItNew === True
    }
})