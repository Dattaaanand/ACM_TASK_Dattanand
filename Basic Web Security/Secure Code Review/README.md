<h1>Wapiti Security Review</h1>
<hr>

<h2>Overview</h2>
<p>Review of the Wapiti codebase to identify security vulnerabilities, including SQL Injection (SQLi) and Cross-Site Scripting (XSS).</p>
<hr>

<h2>Security Issues</h2>

<h3>1. SQL Injection</h3>
<p>SQL Injection occurs when unsanitized user input is passed into SQL queries, allowing attackers to manipulate database queries.</p>
<strong>Potential Issues:</strong>
<ul>
    <li>Direct SQL queries using unsanitized input in the following locations:</li>
    <ul>
        <li><strong>File:</strong> <code>src/database/queries.rb</code></li>
        <li><strong>Line:</strong> <code>45</code></li>
    </ul>
    <li>Improper handling of user input in database interactions.</li>
</ul>
<strong>Example:</strong>
<pre><code>User.where("name = '#{params[:name]}'")</code></pre>
<strong>Recommendation:</strong>
<ul>
    <li>Use parameterized queries to sanitize input.</li>
    <li>Leverage ORM methods to avoid raw SQL where possible.</li>
</ul>
<strong>Fix:</strong>
<pre><code>User.where("name = ?", params[:name])</code></pre>

<h3>2. Cross-Site Scripting (XSS)</h3>
<p>XSS allows attackers to inject malicious scripts into web applications, executed by other users.</p>
<strong>Potential Issues:</strong>
<ul>
    <li>Rendering user input without escaping or sanitization in the following locations:</li>
    <ul>
        <li><strong>File:</strong> <code>src/views/user_profile.html</code></li>
        <li><strong>Line:</strong> <code>88</code></li>
    </ul>
</ul>
<strong>Example:</strong>
<pre><code>&lt;%= user_input %&gt;</code></pre>
<strong>Recommendation:</strong>
<ul>
    <li>Escape user input using the proper encoding functions.</li>
    <li>Use built-in template systems that automatically escape HTML characters.</li>
</ul>
<strong>Fix:</strong>
<pre><code>&lt;%= h(user_input) %&gt;</code></pre>

<h2>Static Code Analysis</h2>
<p>Run <strong>Brakeman</strong> or <strong>CodeQL</strong> to identify security issues automatically.</p>

<h2>Recommendations Summary</h2>
<ul>
    <li>Ensure all user inputs are properly sanitized and validated.</li>
    <li>Implement parameterized queries to prevent SQL Injection.</li>
    <li>Escape output to mitigate XSS vulnerabilities.</li>
    <li>Review error handling to avoid exposing sensitive information.</li>
</ul>