function validate() {
    var username_field = document.getElementById("username")
    var password_field = document.getElementById("password")

    var username_verdict = document.getElementById("username_verdict")
    var password_verdict = document.getElementById("password_verdict")

    if (!username_field)
    {
        return false
    }

    var username = username_field.value
    
    if (password_field)
    {
        var password = password_field.value
    }
    
    if (username)
    {
        if (username.length < 3 || username.length > 15)
        {
            username_verdict.classList.add('invalid')
            username_verdict.classList.remove('valid')

            if (username.length < 3)
            {
                username_verdict.innerHTML = 'Length less than 3'
            }
            else
            {
                username_verdict.innerHTML = 'Length more than 15'
            }

            var res_username = false
        }
        else
        {
            username_verdict.classList.add('valid')
            username_verdict.classList.remove('invalid')

            username_verdict.innerHTML = 'OK'

            var res_username = true
        }
    }
    else
    {
        username_verdict.innerHTML = ''

        var res_username = false
    }

    if (!password_field) return res_username

    if (password)
    {
        if (password.length < 3 || password.length > 80)
        {
            password_verdict.classList.add('invalid')
            password_verdict.classList.remove('valid')

            if (password.length < 3)
            {
                password_verdict.innerHTML = 'Length less than 3'
            }
            else
            {
                password_verdict.innerHTML = 'Length more than 80'
            }

            var res_password = false
        }
        else
        {
            password_verdict.classList.add('valid')
            password_verdict.classList.remove('invalid')

            password_verdict.innerHTML = 'OK'

            var res_password = true
        }
    }
    else
    {
        password_verdict.innerHTML = ''

        var res_password = false
    }

    return res_username && res_password
}

$('#submit').on('click', function(){
    return validate()
})
