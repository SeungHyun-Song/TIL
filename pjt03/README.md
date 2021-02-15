# README

### 1.

```css
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <!-- Bootstrap CSS -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">
  <!-- Custom CSS -->
  <link rel="stylesheet" href="01_nav_footer.css">
  <title>Navbar Footer Test</title>
</head>
<body>

  <nav class="navbar navbar-expand-lg navbar-dark fixed-top bg-dark">
    <div class="container-fluid">
      <a href="02_home.html">
        <img src="images/logo.png" alt="Logo Image">
      </a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav ms-auto mb-2 mb-lg-0">
          <li class="nav-item">
            <a class="nav-link text-decoration-none text-white fw-bold" href="02_home.html">Home</a>
          </li>
          <li class="nav-item">
            <a class="nav-link text-decoration-none text-white" href="03_community.html">Community</a>
          </li>
          <li class="nav-item">
            <a class="nav-link text-decoration-none text-white" href="#"  data-bs-toggle="modal" data-bs-target="#Login">Login</a>
          </li>
        </ul>
      </div>
    </div>
  </nav>

  <div class="modal fade" id="Login" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="LoginLabel">Login</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="close"></button>
        </div>
        <div class="modal-body">
          <div class="mb-3">
            <label for="exampleInputEmail1" class="form-label fw-bold">Username</label>
            <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp">
          </div>
          <div class="mb-3">
            <label for="exampleInputPassword1" class="form-label fw-bold">Password</label>
            <input type="password" class="form-control" id="exampleInputPassword1">
          </div>
          <div class="mb-4 form-check d-flex justify-content-between">
            <div>
              <input type="checkbox" class="form-check-input" id="exampleCheck1">
              <label class="form-check-label" for="exampleCheck1">check me out</label>
            </div>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
            <button type="button" class="btn btn-primary">Submit</button>
          </div>
        </div>
      </div>
    </div>
  </div>

    
  <footer class="fixed-bottom">
    <p>Web-bootstrap PJT, by SSH</p>
  </footer>

  <!-- Bootstrap JS -->
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/js/bootstrap.bundle.min.js" integrity="sha384-ygbV9kiqUc6oa4msXn9868pTtWMgiQaeYH7/t7LECLbyPA2x65Kgf80OJFdroafW" crossorigin="anonymous"></script>
</body>
</html>
```

```css
/* 01_nav_footer.css */
/* 아래에 코드를 작성해 주세요. */

body {
  height: 3000px;
}

/* nav {
  height: 60px;
} */

nav img {
  height: 60px;
}

footer {
  display: flex;
  justify-content: center;
  align-items: center;
  margin: 1rem 0;
}
```

#### 어디서 이렇게 막혔지??

* 원인 1
  * nav { height: 60px; }로 해놓고 navbar에 toggle 적용하려니 흰 바탕에 흰색글자.
  * 토글로 늘어난 메뉴 안의 글자들이 보이지 않았고 그 원인은 navbar의 길이 고정에 의해 검은색인 navbar의 확장이 이루어지지 않은 것.
* 원인 2
  * toggle, modal 설정 미숙.
  * data-bs-toggle="collapse", data-bs-toggle="modal", data-bs-target="#Login" 등에서 bs를 쓰지 않은 것. 적어주는 이유는 아직도 잘 모르겠음...
* 원인 3
  * modal 안에서의 Login 양식 작성 미숙.



### 2.

```css
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <!-- Bootstrap CSS -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">
  <!-- Custom CSS -->
  <link rel="stylesheet" href="01_nav_footer.css">
  <link rel="stylesheet" href="02_home.css">
  <title>Home</title>
</head>
<body>

  <nav class="navbar navbar-expand-lg navbar-dark fixed-top bg-dark">
    <div class="container-fluid">
      <a href="02_home.html">
        <img src="images/logo.png" alt="Logo Image">
      </a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav ms-auto mb-2 mb-lg-0">
          <li class="nav-item">
            <a class="nav-link text-decoration-none text-white fw-bold" href="02_home.html">Home</a>
          </li>
          <li class="nav-item">
            <a class="nav-link text-decoration-none text-white" href="03_community.html">Community</a>
          </li>
          <li class="nav-item">
            <a class="nav-link text-decoration-none text-white" href="#"  data-bs-toggle="modal" data-bs-target="#Login">Login</a>
          </li>
        </ul>
      </div>
    </div>
  </nav>

  <div class="modal fade" id="Login" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="LoginLabel">Login</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="close"></button>
        </div>
        <div class="modal-body">
          <div class="mb-3">
            <label for="exampleInputEmail1" class="form-label fw-bold">Username</label>
            <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp">
          </div>
          <div class="mb-3">
            <label for="exampleInputPassword1" class="form-label fw-bold">Password</label>
            <input type="password" class="form-control" id="exampleInputPassword1">
          </div>
          <div class="mb-4 form-check d-flex justify-content-between">
            <div>
              <input type="checkbox" class="form-check-input" id="exampleCheck1">
              <label class="form-check-label" for="exampleCheck1">check me out</label>
            </div>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
            <button type="button" class="btn btn-primary">Submit</button>
          </div>
        </div>
      </div>
    </div>
  </div>
  
  <header>
    <div id="carouselExampleSlidesOnly" class="carousel slide" data-bs-ride="carousel">
      <div class="carousel-inner">
        <div class="carousel-item active">
          <img src="images/header1.jpg" class="d-block w-100" alt="...">
        </div>
        <div class="carousel-item">
          <img src="images/header2.jpg" class="d-block w-100" alt="...">
        </div>
        <div class="carousel-item">
          <img src="images/header3.jpg" class="d-block w-100" alt="...">
        </div>
      </div>
    </div>
  </header>

  <h1 class="text-center my-5">Boxoffice</h1>


  <section>
    <article>
      <div class="movie-list">
        <div class="row row-cols-1 row-cols-md-2 row-cols-lg-3 g-4">
          <div class="card">
            <img src="images/movie1.jpg" class="card-img-top" alt="movie1">
            <div class="card-body">
              <h5 class="card-title">Movie Title</h5>
              <p class="card-text">This is a longer card with supportin text below as....</p>
            </div>
          </div>
          <div class="card">
            <img src="images/movie2.jpg" class="card-img-top" alt="movie2">
            <div class="card-body">
              <h5 class="card-title">Movie Title</h5>
              <p class="card-text">This is a longer card with supportin text below as....</p>
            </div>
          </div>
          <div class="card">
            <img src="images/movie3.jpg" class="card-img-top" alt="movie3">
            <div class="card-body">
              <h5 class="card-title">Movie Title</h5>
              <p class="card-text">This is a longer card with supportin text below as....</p>
            </div>
          </div>
          <div class="card">
            <img src="images/movie4.jpg" class="card-img-top" alt="movie4">
            <div class="card-body">
              <h5 class="card-title">Movie Title</h5>
              <p class="card-text">This is a longer card with supportin text below as....</p>
            </div>
          </div>
          <div class="card">
            <img src="images/movie5.jpg" class="card-img-top" alt="movie5">
            <div class="card-body">
              <h5 class="card-title">Movie Title</h5>
              <p class="card-text">This is a longer card with supportin text below as....</p>
            </div>
          </div>
          <div class="card">
            <img src="images/movie6.jpg" class="card-img-top" alt="movie6">
            <div class="card-body">
              <h5 class="card-title">Movie Title</h5>
              <p class="card-text">This is a longer card with supportin text below as....</p>
            </div>
          </div>
        </div>
      </div>
    </article>

  </section>

  <!-- 01_nav_footer.html -->
  <footer class="fixed-bottom">
    <p>Web-bootstrap PJT, by SSH</p>
  </footer>


  <!-- Bootstrap JS -->
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/js/bootstrap.bundle.min.js" integrity="sha384-ygbV9kiqUc6oa4msXn9868pTtWMgiQaeYH7/t7LECLbyPA2x65Kgf80OJFdroafW" crossorigin="anonymous"></script>
</body>
</html>
```

```css
/* 02_home.css */
/* 아래에 코드를 작성해 주세요. */

body {
  height: 3000px;
}

nav img {
  height: 60px;
}

header {
  margin-top: 75px;
}
footer {
  display: flex;
  justify-content: center;
  align-items: center;
  margin: 1rem 0;
}
```

#### 어디서 이렇게 막혔지??

* 원인 1
  * card 의 화면 크기에 따른 배치 미숙
  * row row-cols-1 row-cols-md-2 row-cols-lg-3 g-4 라고 작성
  * 일렬로 나열, 가로길이 576px미만일 때 1개 표시, 576px 이상 992px미만일 때 2개 표시, 그 이상 3개 표시, 사이 간격은 4rem 으로 고정.
  * 이 표현을 충분히 숙지할 필요 있음.
* 원인 2
  * 쓸데없는 `<a href>`의 작성으로 카드 내의 문자들이 링크처럼 밑줄 그이고 파란색으로, 클릭 되게 만들어짐.

### 3.

```css

```

```css

```

