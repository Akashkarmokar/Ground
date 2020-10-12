
function copyText() {
    var copyText = document.getElementById("copyText");
    copyText.select();
    copyText.setSelectionRange(0, 99999)
    alert("Copied : " + copyText.value);
}