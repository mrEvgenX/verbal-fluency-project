<template>
    <div>
        <h1>Регистрация</h1>
        <form action="" method="post">
            <div class="form-group">
                <input class="form-control" type="email" name="login" id="login" placeholder="Адрес электронной почты">
            </div>
            <div class="form-group">
                <input class="form-control" type="password" name="pass" id="pass" placeholder="Пароль">
            </div>
            <div class="form-group">
                <input class="form-control" type="password" name="pass-repeat" id="pass-repeat" placeholder="Пароль еще раз">
            </div>
            <button class="btn btn-primary" type="submit">Регистрация</button>
        </form>
    </div>
</template>

<script>
export default {
    name: 'Register',
}
</script>