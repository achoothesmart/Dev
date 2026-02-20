import { AppComponent } from "./app.component";
export function sayHello(component: AppComponent){
    prompt('Title:  ' + component.title)
}