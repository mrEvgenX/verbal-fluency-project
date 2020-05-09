<template>
    <div>
        <h1>Профиль</h1>
        <h3>Смена почтового адреса</h3>
        <p>address@mail.ru</p>
        <form action="" method="post">
            <div class="form-group">
                <input class="form-control" type="email" name="login" id="login" placeholder="Новый адрес электронной почты">
            </div>
            <button class="btn btn-primary" type="submit">Сменить адрес почты</button>
        </form>
        <h3>Смена пароля</h3>
        <form action="" method="post">
            <div class="form-group">
                <input class="form-control" type="password" name="old-pass" id="old-pass" placeholder="Текущий пароль">
            </div>
            <div class="form-group">
                <input class="form-control" type="password" name="new-pass" id="new-pass" placeholder="Новый пароль">
            </div>
            <div class="form-group">
                <input class="form-control" type="password" name="new-pass-repeat" id="new-pass-repeat" placeholder="Новый пароль еще раз">
            </div>
            <button class="btn btn-primary" type="submit">Поменять пароль</button>
        </form>
    </div>
</template>

<script>
export default {
    name: 'Profile',
}
</script>