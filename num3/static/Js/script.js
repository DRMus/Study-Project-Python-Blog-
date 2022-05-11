function page_count(page){
    if (page != 'None'){
        window.location.href = "/users/"+page
    }
}

function profile(id){
    window.location.href = "/users/id"+id
}