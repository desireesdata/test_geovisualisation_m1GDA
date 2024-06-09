function findGetParameter(parameterName) {
    let result = null,
        tmp = [];
    let items = location.search.substr(1).split("&");
    for (var index = 0; index < items.length; index++) {
        tmp = items[index].split("=");
        if (tmp[0] === parameterName) result = decodeURIComponent(tmp[1]);
    }
    return result;
}

function editor() {
    if(!this.classList.contains('richText-initial')) {

        $(this).richText({
            // text formatting
            bold: true,
            italic: true,
            underline: true,
    
            // text alignment
            leftAlign: true,
            centerAlign: true,
            rightAlign: true,
            justify: true,
    
            // lists
            ol: true,
            ul: true,
    
            // title
            heading: true,
    
            // fonts
            fonts: true,
            fontList: ["Arial",
                "Arial Black",
                "Comic Sans MS",
                "Courier New",
                "Geneva",
                "Georgia",
                "Helvetica",
                "Impact",
                "Lucida Console",
                "Tahoma",
                "Times New Roman",
                "Verdana"
            ],
            fontColor: true,
            fontSize: true,
    
            // uploads
            imageUpload: true,
            fileUpload: true,
    
            // link
            urls: true,
    
            // tables
            table: true,
    
            // code
            removeStyles: true,
            code: true,
    
            // colors
            colors: [],
    
            // dropdowns
            fileHTML: '',
            imageHTML: '',
    
            // privacy
            youtubeCookies: false,
        
            // dev settings
            useSingleQuotes: false,
            height: 0,
            heightPercentage: 0,
            id: "",
            class: "",
            useParagraph: false,
            maxlength: 0,
        
            // callback function after init
            callback: undefined
        });
    }
}

function w3IncludeHTML() {
    var z, i, a, file, xhttp;
    z = document.getElementsByTagName("*");
    for (i = 0; i < z.length; i++) {
        if (z[i].getAttribute("w3-include-html")) {
        a = z[i].cloneNode(false);
        file = z[i].getAttribute("w3-include-html");
        xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function() {
            if (this.readyState == 4 && this.status == 200) {
            a.removeAttribute("w3-include-html");
            a.innerHTML = this.responseText;
            z[i].parentNode.replaceChild(a, z[i]);
            //          w3IncludeHTML();
            }
        }
        xhttp.open("GET", file, true);
        xhttp.send();
        return;
        }
    }
}

function preparaadvertencia(advertencia, nom, tipus, text, i = null) {
    let elements = document.getElementsByName(nom);
    if(i != null) {
        e = i;
        elements[e].onfocus = function() {
            if(tipus == 'input') {
                advertencia.textContent = "[Caràcters: " + elements[e].value.length + text;
            } else {
                advertencia.textContent = text;
            }
        };
        if(tipus == 'input') {
            elements[e].oninput = function() {
                advertencia.textContent = "[Caràcters: " + elements[e].value.length + text;
            };
        }
    } else {
        for(let e = 0; e < elements.length; e++) {
            elements[e].onfocus = function() {
                if(tipus == 'input') {
                    advertencia.textContent = "[Caràcters: " + elements[e].value.length + text;
                } else {
                    advertencia.textContent = text;
                }
            };
            if(tipus == 'input') {
                elements[e].oninput = function() {
                    advertencia.textContent = "[Caràcters: " + elements[e].value.length + text;
                };
            }
        }
    }
}

var lang = null;
var numberOfLanguages = 26;