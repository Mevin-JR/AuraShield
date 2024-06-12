const body = document.getElementById('body');

window.addEventListener('load', () => {
    const loader = document.getElementById("loader");
    loader.classList.add('loader-hidden');
    loader.addEventListener('transitionend', () => {
        loader.parentNode.removeChild(loader); // TODO: Fix this
    });
});

const popupContainer = document.querySelector('.popup');
const shortTextInput = document.getElementById('method-1');
const shortTextPopup = document.getElementById('short-text');
const textInput = document.getElementById('method-2');
const textInputPopup = document.getElementById('text-input');
const imageInput = document.getElementById('method-3');
const imageInputPopup = document.getElementById('image-input');
const ingInput = document.getElementById('method-4');
const ingInputPopup = document.getElementById('ing-input');

const cancelBtn = document.getElementById('cancel-btn');

function closePopup() {
    popupContainer.style.visibility = 'hidden';
    shortTextPopup.style.visibility = 'hidden';
    textInputPopup.style.visibility = 'hidden';
    imageInputPopup.style.visibility = 'hidden';
    ingInputPopup.style.visibility = 'hidden';
    body.style.overflow = 'auto';
}

shortTextInput.addEventListener('click', () => {
    popupContainer.style.visibility = 'visible';
    shortTextPopup.style.visibility = 'visible';
    body.style.overflow = 'hidden';
});

textInput.addEventListener('click', () => {
    popupContainer.style.visibility = 'visible';
    textInputPopup.style.visibility = 'visible';
    body.style.overflow = 'hidden';
});

imageInput.addEventListener('click', () => {
    popupContainer.style.visibility = 'visible';
    imageInputPopup.style.visibility = 'visible';
    body.style.overflow = 'hidden';
});

ingInput.addEventListener('click', () => {
    popupContainer.style.visibility = 'visible';
    ingInputPopup.style.visibility = 'visible';
    body.style.overflow = 'hidden';
});

cancelBtn.addEventListener('click', (event) => {
    event.preventDefault();
});

const rBrand = document.getElementById('result-brand');
const rProduct = document.getElementById('result-product');
const rIngredients = document.getElementById('result-ingredients');
const rSkinType = document.getElementById('result-skintype');
const rToxins = document.getElementById('result-toxins');
const rToxicity = document.getElementById('result-toxicity');

const rtContainer = document.getElementById('result-toxin-container');
const result = document.getElementById('result');
const tResult = document.getElementById('toxicity-result');
const stForm = document.getElementById('short-text');
const tiForm = document.getElementById('text-input');
const iIForm = document.getElementById('ing-input');

const errorMsg = document.getElementById('error-msg');

stForm.addEventListener('submit', (event) => {
    event.preventDefault();

    var formData = new FormData(stForm);

    fetch('/short-text', {
        method: "POST",
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        const brand = data.brand
        const product = data.product_name
        const ingredients = data.ingredients
        const skinType = data.skin_type
        const toxins = data.toxins

        rBrand.innerText = brand;
        rProduct.innerText = product;
        rIngredients.innerText = ingredients;
        rSkinType.innerText = skinType;
        if (toxins > 0) {
            rToxins.innerHTML = `<span style="color: red !important;">${toxins} potential toxin(s)</span> found in ingredients`;
        }else {
            rToxins.innerHTML = `<span style="color: green !important;">${toxins} potential toxin(s)</span> found in ingredients`;
        }

        rtContainer.style.display = 'block';
        result.style.display = 'inline-block';
        tResult.style.display = 'none';
        window.location.href = '/database#result';
        closePopup()
    })
    .catch(error => {
        console.log('Error', error);
        closePopup()
        popupContainer.style.visibility = 'visible';
        errorMsg.style.visibility = 'visible';
        body.style.overflow = 'hidden';
    });
});

tiForm.addEventListener('submit', (event) => {
    event.preventDefault();

    var formData = new FormData(tiForm);

    fetch('/text-input', {
        method: "POST",
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        const brand = data.brand
        const product = data.product_name
        const ingredients = data.ingredients
        const skinType = data.skin_type
        const toxins = data.toxins

        rBrand.innerText = brand;
        rProduct.innerText = product;
        rIngredients.innerText = ingredients;
        rSkinType.innerText = skinType;
        if (toxins > 0) {
            rToxins.innerHTML = `<span style="color: red !important;">${toxins} potential toxin(s)</span> found in ingredients`;
        }else {
            rToxins.innerHTML = `<span style="color: green !important;">${toxins} potential toxin(s)</span> found in ingredients`;
        }

        rtContainer.style.display = 'block';
        result.style.display = 'inline-block';
        tResult.style.display = 'none';
        window.location.href = '/database#result';
        closePopup()
    })
    .catch(error => {
        console.log('Error', error);
        closePopup()
        popupContainer.style.visibility = 'visible';
        errorMsg.style.visibility = 'visible';
        body.style.overflow = 'hidden';
    });
});

iIForm.addEventListener('submit', (event) => {
    event.preventDefault();

    var formData = new FormData(iIForm);

    fetch('/ing-input', {
        method: "POST",
        body: formData
    })
    .then(response => response.json())
    .then(data => {

        if (data.result == "list") {
            if (data.toxins > 0) {
                rToxicity.innerHTML = `Provided ingredients contains <span style="color: red !important;">${data.toxins} potential toxin(s)</span>`;
            } else {
                rToxicity.innerHTML = `Provided ingredients contains <span style="color: green !important;">${data.toxins} potential toxin(s)</span>`;
            }
        } else {
            let output;
            if (data.isToxic === 1) {
                output = `Ingredient (${data.ingredient}) is <span style="color: red !important;"> potentialy harmful</span>`
                rToxicity.innerHTML = output;
            } else if (data.isToxic === 0) {
                output = `Ingredient (${data.ingredient}) is <span style="color: green !important;">not harmful</span>`
                rToxicity.innerHTML = output;
            } else if (data.isToxic === -1) {
                output = `Could not identify ${data.ingredient}`
                rToxicity.innerText = output;
            } else {
                output = "Something went wrong! Try again"
                rToxicity.innerText = output;
            }
        }

        rtContainer.style.display = 'block';
        tResult.style.display = 'inline-block';
        result.style.display = 'none';
        window.location.href = '/database#toxicity-result';
        closePopup()
    })
    .catch(error => {
        console.log('Error', error);
        closePopup()
        popupContainer.style.visibility = 'visible';
        errorMsg.style.visibility = 'visible';
        body.style.overflow = 'hidden';
    });
});