

function getArr(){
    let arr = localStorage.getItem('var');
    if(arr == null || arr == 'null'){
        arr = []
    } else {
        arr = JSON.parse(localStorage.getItem('var'));
    }
    return arr;
}

function setArr(arr){
    localStorage.setItem('var', JSON.stringify(arr));
}


function removeLocalStorage(){
    localStorage.removeItem('var');
}





$(document).on('change', '.my_radio', function(){

    let tqk_id = $(this).attr('data-task-id') - 1;
    let option_id = $(this).attr('data-option-id');
    let arr = getArr();
    arr[task_id] = option_id;
    setArr(arr);

    console.log(getArr());
});


//$('#myTabs a').click(function (e) {
//  e.preventDefault()
//  $(this).tab('show')
//})


$(document).on('click', '.button', function(){

    let data = {}; // form data

    $.ajax({
        url: '/sendData',
        method: 'POST',
        data: data,
        
    });



});

