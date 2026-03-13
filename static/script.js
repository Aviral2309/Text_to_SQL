function fillExample(text){
document.getElementById("question").value = text
}

async function ask(){

const question = document.getElementById("question").value

if(!question) return

document.getElementById("loading").style.display="block"

const response = await fetch("/query",{
method:"POST",
headers:{
"Content-Type":"application/json"
},
body:JSON.stringify({
question:question
})
})

const data = await response.json()

document.getElementById("loading").style.display="none"

document.getElementById("sql").innerText = data.sql_query

renderTable(data.result)

}

function renderTable(data){

const container = document.getElementById("result")

if(!data || data.length === 0){
container.innerHTML = "No results"
return
}

let table = "<table>"

const headers = Object.keys(data[0])

table += "<tr>"

headers.forEach(function(h){
table += "<th>" + h + "</th>"
})

table += "</tr>"

data.forEach(function(row){

table += "<tr>"

headers.forEach(function(h){
table += "<td>" + row[h] + "</td>"
})

table += "</tr>"

})

table += "</table>"

container.innerHTML = table

}

document.getElementById("question")
.addEventListener("keypress",function(e){

if(e.key === "Enter"){
ask()
}

})