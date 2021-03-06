import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';


import { AppComponent } from './app.component';
import { MyComponentComponent } from './my-component/my-component.component';

//Added by Mitchell
import { FormsModule } from '@angular/forms'; 
import { HttpModule } from '@angular/http'; 


@NgModule({
  declarations: [
    AppComponent,
    MyComponentComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
