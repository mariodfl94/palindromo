function pal(str) {
    const strn = str.replace(/[\W_]/g, "")
                    .toLowerCase();
    const revertido = strn.split("")
                    .reverse()
                    .join("");

    return strn == revertido ? "es palindromo" : "no es palindromo";
}
console.log(pal("hola mundo")); 
