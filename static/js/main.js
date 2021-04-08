window.onload = function() {
    var div = document.getElementsByTagName('code');
    for (let i = 0; i<div.length; i++){
        div[i].onclick = function(e) {
            this.contentEditable = true;
            this.parentNode.parentNode.open = false;
        }
    }
}


function getContent(){
    let idx=1, in_idx=1, Arr=Array();
    let counter=0;
    while (1) {
        if (document.getElementById(idx) && (Arr.length < idx)) { 
            Arr.push({
                "name": document.getElementById(idx).value,
                "scenario": Array()
            })
        }
        value = idx.toString() + '.' +   in_idx.toString()
        console.log(Arr, value, idx, in_idx)
        if (document.getElementById(value)){
            if (document.getElementById(value).checked){
                Arr[Arr.length - 1]['scenario'].push(document.getElementsByTagName("summary")[counter].textContent.trim())
            }
            counter += 1
            in_idx += 1
        }
        else{
            idx += 1
            in_idx = 1
            
            if (!document.getElementById(idx.toString() + '.1')){
                document.getElementById("scenario").value = JSON.stringify(Arr);
                return
            }
        }
    }
} 

let elements = document.getElementsByTagName('input');
for (let i=0; i<elements.length; i++) {
    elements[i].addEventListener('click', function() {
        let input = this;
        let li = input.parentNode.parentNode.parentNode.parentNode;
        if (input.checked) {
            li.classList.remove('excluded');
        } else {
            li.classList.add('excluded');
        }
    });
}
