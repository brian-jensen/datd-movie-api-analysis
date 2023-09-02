### Directions on How to Run the Project Locally
<style>
  ol > li {
    margin: 8px 0;
  }
  ul {
    padding-left: 15px;
  }
</style>
<ol>
  <li><strong>Clone the Repo</li></strong>
  <li><strong>Create a Virtual Environment</strong>
    <ul>
      <li><code>python3 -m venv env</code> (Mac/Linux)</li>
      <li><code>python -m venv env</code> (Windows)</li>
    </ul>
  </li>
  <li><strong>Activate the Virtual Environment</strong>
    <ul>
      <li><code>source ./env/bin/activate</code> (Mac/Linux)</li>
      <li><code>.\env\Scripts\activate</code> (Windows)</li>
    </ul>
  </li>
  <li><strong>Install the Requirements</strong>
    <ul>
      <li><code>pip install -r requirements.txt</code></li>
    </ul>
  </li>
  <li><strong>Working with the OMDb API</strong>
    <ul>
      <li>Apply for an OMDb &#8674; <a href="http://www.omdbapi.com/apikey.aspx" target="_blank">API Key</a> &#8672;</li>
      <li>Create a <code>.env</code> file in the root directory of the project.</li>
      <li>Inside the <code>.env</code> file add <code>api_key=yourkey</code></li>
    </ul>
  </li>
  <li><strong>Run the movie_requests.py File</strong>
    <ul>
      <li><code>python3 movie_requests.py</code> (Mac/Linux)</li>
      <li><code>python movie_requests.py</code> (Windows)</li>
    </ul>
  </li>
</ol>