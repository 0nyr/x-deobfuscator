
falsyCharsRegex = [
    /‍/g, // U+200D
    / /g, // U+2002
    / /g // U+2003
];

function clearContents(element) {
    element.value = '';
}

// deobfuscate functions
function areFalsyCharactersPresent(str) {
    let result = false;
    // use every instead of forEach() https://masteringjs.io/tutorials/fundamentals/foreach-break
    // stops iterating through the array whenever the callback function returns a falsy value.
    falsyCharsRegex.every((regex) => {
        if(str.search(regex) != -1) {
            result = true;
            return false;
        }
        return true;
    });
    return result;
}

function checkFalsyCharactersPresence(str) {
    if(areFalsyCharactersPresent(str)) {
        console.log("falsy chars found");
    } else {
        console.log("no falsy chars found");
    }
}

function cleanStrFromFalsyChars(str) {
    falsyCharsRegex.forEach((regex) => {
        str = str.replace(regex, "");
    });
    return str;
}

// button functions
function deobfuscate(idTextarea) {
    console.log("deobfuscate");
    let code = document.getElementById(idTextarea).value;
    console.log(code);

    // test presence of falsy characters
    checkFalsyCharactersPresence(code);

    // clean from falsy characters
    console.log("cleaning code");
    code = cleanStrFromFalsyChars(code);

    // test presence of falsy characters
    checkFalsyCharactersPresence(code);

    document.getElementById("result_textarea").value = code;
}

function clearTextarea(textareaIds) {
    console.log(textareaIds.toString());
    console.log(typeof(textareaIds));
    textareaIds.forEach((id) => {
        console.log("id = ", id);
        //clearContents(document.getElementById(id));
        document.getElementById(id).value = "";
    });
}