$(document).ready(() => {
    let addBtn = $('#add_btn')
    let searchBox = $('#search_key')
    let pokeBoxes = $('.pokemon-box-container')
    let baseURL = window.origin

    // search proccess, filter when searching
    searchBox.keyup((e) => {
        let searchKey = e.target.value.toLowerCase()

        pokeBoxes.each((index, box) => {
            name = box.title.toLowerCase()

            if (name.indexOf(searchKey) > -1) {
                box.style.display = ''
            } else {
                box.style.display = 'none'
            }
        })
    })

    // add button click
    addBtn.click(() => {
        location.href =  `${ baseURL }/add-pokemon`
    })

    // on click pokemon box
    pokeBoxes.click((e) => {
        name = e.currentTarget.title
        location.href =  `${ baseURL }/pokemons/${ name }`
    })
})