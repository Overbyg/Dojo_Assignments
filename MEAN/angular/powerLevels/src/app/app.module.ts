import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';


import { AppComponent } from './app.component';
import { HumanComponent } from './human/human.component';
import { SaiyanComponent } from './saiyan/saiyan.component';
import { SupersaiyanComponent } from './supersaiyan/supersaiyan.component';
import { SupersaiyantwoComponent } from './supersaiyantwo/supersaiyantwo.component';
import { SupersaiyanthreeComponent } from './supersaiyanthree/supersaiyanthree.component';
import { SupersaiyanfourComponent } from './supersaiyanfour/supersaiyanfour.component';

import { FormsModule } from '@angular/forms'; // <-- Import FormsModule
import { HttpModule } from '@angular/http'; // <-- Import HttpModule


@NgModule({
  declarations: [
    AppComponent,
    HumanComponent,
    SaiyanComponent,
    SupersaiyanComponent,
    SupersaiyantwoComponent,
    SupersaiyanthreeComponent,
    SupersaiyanfourComponent
  ],
  imports: [
    BrowserModule,
    FormsModule, // <-- Include module in our AppModules
		HttpModule // <-- Include module in our AppModules
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
