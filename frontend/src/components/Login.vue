<template>
    <div>
        <h1>Вход</h1>
        <form action="" method="post">
            <div class="form-group">
                <input class="form-control" type="text" name="email" id="email" placeholder="Адрес электронной почты">
            </div>
            <div class="form-group">
                <input class="form-control" type="password" name="pass" id="pass" placeholder="Пароль">
            </div>
            <button class="btn btn-primary" type="submit">Вход</button>
        </form>
    </div>
</template>

<script>
export default {
    name: 'Login',
}
</script>