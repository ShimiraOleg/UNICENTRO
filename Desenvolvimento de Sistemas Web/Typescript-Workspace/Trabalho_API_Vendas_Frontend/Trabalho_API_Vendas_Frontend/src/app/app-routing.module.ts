import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import {UserLoginComponent} from "src/app/view/user-login/user-login.component"
import { HomeComponent } from './view/home/home.component';

const routes: Routes = [
  {
    path: "home",
    component: HomeComponent
  },
  {
    path: "login",
    component: UserLoginComponent
  },
  {
    path: "**",
    redirectTo: "/home"
  },
  {
    path: '',
    redirectTo: '/home',
    pathMatch: 'full'
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
