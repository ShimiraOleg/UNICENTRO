import { Component } from '@angular/core';
import { User } from 'src/app/model/user';
import { AuthService } from 'src/app/services/auth.service';
import { UserService } from 'src/app/services/user.service';

@Component({
  selector: 'app-user-login',
  templateUrl: './user-login.component.html',
  styleUrls: ['./user-login.component.css']
})
export class UserLoginComponent {
  constructor(private userService: UserService, private authService: AuthService) {
    this.login();
  }

  login(): void {
    const user = new User();
    user.email = "zombiew123@gmail.com"
    user.password = "123456"
    this.userService.createSession(user).subscribe({
      next: (res) =>{
        this.authService.mockUserLogin(res);
      }, error: (err) =>{
        console.log('login failed', err)
      }
    })
  }
}
