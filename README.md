
<h1>WhatsApp Message Automation</h1>

<p>This project automates sending personalized WhatsApp messages using Python. It reads a list of contacts from a text file and sends messages with a personalized greeting and CNPJ reference.</p>

<h2>Features</h2>
<ul>
    <li>Reads contacts from a semicolon-separated text file (<code>lista.txt</code>)</li>
    <li>Extracts and capitalizes the first name of each contact</li>
    <li>Validates phone numbers and CNPJ</li>
    <li>Sends personalized messages via WhatsApp Web using <code>pywhatkit</code></li>
    <li>Activates WhatsApp Web window and clicks the send button using <code>pyautogui</code></li>
    <li>Closes the active Google Chrome tab after sending each message</li>
</ul>

<h2>Requirements</h2>
<ul>
    <li>Python 3.x</li>
    <li><code>pandas</code></li>
    <li><code>pywhatkit</code></li>
    <li><code>pyautogui</code></li>
    <li><code>datetime</code></li>
</ul>

<h2>Usage</h2>
<ol>
    <li>Ensure the required libraries are installed:
        <pre><code>pip install pandas pywhatkit pyautogui</code></pre>
    </li>
    <li>Prepare a text file named <code>lista.txt</code> with the following structure:
        <pre><code>nome;telefone;cnpj</code></pre>
    </li>
    <li>Run the script:
        <pre><code>send.py</code></pre>
    </li>
</ol>

<h2>UserScript</h2>

<p>To circumvent the issue of clicking the send button, we use a UserScript. Below is the UserScript code, which is designed to run on macOS Ventura with Python 3.11.5:</p>

<pre><code>
// ==UserScript==
// @name         WhatsApp Web AutoClick
// @namespace    http://tampermonkey.net/
// @version      2024-06-11
// @description  Clica no OK
// @author       You
// @match        *://*.whatsapp.com/*
// @icon         https://www.google.com/s2/favicons?sz=64&domain=whatsapp.com
// @require      https://code.jquery.com/jquery-3.6.4.min.js
// @grant        none
// ==/UserScript==

(function() {
    'use strict';

    // Função para clicar no botão de envio
    function clickSendButton() {
        // Aguarda 30 segundos para a página carregar completamente
        setTimeout(function() {
            // Encontra o botão de envio
            var sendButton = $("div._ak1t._ak1u button");

            // Clica no botão de envio
            sendButton.click();
        }, 30000);
    }

    // Inicia o processo de clicar no botão de envio
    clickSendButton();
})();
</code></pre>

<p>This UserScript is used to automatically click the send button on WhatsApp Web. It is particularly useful for bypassing manual clicks and is implemented on macOS Ventura with Python 3.11.5.</p>

<h2>Notes</h2>
<ul>
    <li>The script relies on a <code>send_button.png</code> image to locate the send button in WhatsApp Web. Make sure this image is available in the same directory as the script.</li>
    <li>Adjust the sleep durations if necessary to match your system's performance.</li>
</ul>

</body>
</html>
