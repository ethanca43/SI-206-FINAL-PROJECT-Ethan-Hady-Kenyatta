"use strict";(self.webpackChunk_N_E=self.webpackChunk_N_E||[]).push([[2086],{67760:function(e,t,r){let n,a,i,o;r.d(t,{u:function(){return Q}});var s=r(78346),l=r.t(s,2);function u(){for(var e=arguments.length,t=Array(e),r=0;r<e;r++)t[r]=arguments[r];return Array.from(new Set(t.flatMap(e=>"string"==typeof e?e.split(" "):[]))).filter(Boolean).join(" ")}function c(e,t){for(var r=arguments.length,n=Array(r>2?r-2:0),a=2;a<r;a++)n[a-2]=arguments[a];if(e in t){let r=t[e];return"function"==typeof r?r(...n):r}let i=Error(`Tried to handle "${e}" but there is no handler defined. Only defined handlers are: ${Object.keys(t).map(e=>`"${e}"`).join(", ")}.`);throw Error.captureStackTrace&&Error.captureStackTrace(i,c),i}var d=((n=d||{})[n.None=0]="None",n[n.RenderStrategy=1]="RenderStrategy",n[n.Static=2]="Static",n),f=((a=f||{})[a.Unmount=0]="Unmount",a[a.Hidden=1]="Hidden",a);function p(e){let{ourProps:t,theirProps:r,slot:n,defaultTag:a,features:i,visible:o=!0,name:s}=e,l=h(r,t);if(o)return m(l,n,a,s);let u=null!=i?i:0;if(2&u){let{static:e=!1,...t}=l;if(e)return m(t,n,a,s)}if(1&u){let{unmount:e=!0,...t}=l;return c(e?0:1,{0:()=>null,1:()=>m({...t,hidden:!0,style:{display:"none"}},n,a,s)})}return m(l,n,a,s)}function m(e){let t=arguments.length>1&&void 0!==arguments[1]?arguments[1]:{},r=arguments.length>2?arguments[2]:void 0,n=arguments.length>3?arguments[3]:void 0,{as:a=r,children:i,refName:o="ref",...l}=b(e,["unmount","static"]),c=void 0!==e.ref?{[o]:e.ref}:{},d="function"==typeof i?i(t):i;"className"in l&&l.className&&"function"==typeof l.className&&(l.className=l.className(t));let f={};if(t){let e=!1,r=[];for(let[n,a]of Object.entries(t))"boolean"==typeof a&&(e=!0),!0===a&&r.push(n);e&&(f["data-headlessui-state"]=r.join(" "))}if(a===s.Fragment&&Object.keys(v(l)).length>0){if(!(0,s.isValidElement)(d)||Array.isArray(d)&&d.length>1)throw Error(['Passing props on "Fragment"!',"",`The current component <${n} /> is rendering a "Fragment".`,"However we need to passthrough the following props:",Object.keys(l).map(e=>`  - ${e}`).join(`
`),"","You can apply a few solutions:",['Add an `as="..."` prop, to ensure that we render an actual element instead of a "Fragment".',"Render a single element as the child so that we can forward the props onto that element."].map(e=>`  - ${e}`).join(`
`)].join(`
`));let e=d.props,t="function"==typeof(null==e?void 0:e.className)?function(){for(var t=arguments.length,r=Array(t),n=0;n<t;n++)r[n]=arguments[n];return u(null==e?void 0:e.className(...r),l.className)}:u(null==e?void 0:e.className,l.className);return(0,s.cloneElement)(d,Object.assign({},h(d.props,v(b(l,["ref"]))),f,c,function(){for(var e=arguments.length,t=Array(e),r=0;r<e;r++)t[r]=arguments[r];return{ref:t.every(e=>null==e)?void 0:e=>{for(let r of t)null!=r&&("function"==typeof r?r(e):r.current=e)}}}(d.ref,c.ref),t?{className:t}:{}))}return(0,s.createElement)(a,Object.assign({},b(l,["ref"]),a!==s.Fragment&&c,a!==s.Fragment&&f),d)}function h(){for(var e=arguments.length,t=Array(e),r=0;r<e;r++)t[r]=arguments[r];if(0===t.length)return{};if(1===t.length)return t[0];let n={},a={};for(let e of t)for(let t in e)t.startsWith("on")&&"function"==typeof e[t]?(null!=a[t]||(a[t]=[]),a[t].push(e[t])):n[t]=e[t];if(n.disabled||n["aria-disabled"])return Object.assign(n,Object.fromEntries(Object.keys(a).map(e=>[e,void 0])));for(let e in a)Object.assign(n,{[e](t){for(var r=arguments.length,n=Array(r>1?r-1:0),i=1;i<r;i++)n[i-1]=arguments[i];for(let r of a[e]){if((t instanceof Event||(null==t?void 0:t.nativeEvent)instanceof Event)&&t.defaultPrevented)return;r(t,...n)}}});return n}function g(e){var t;return Object.assign((0,s.forwardRef)(e),{displayName:null!=(t=e.displayName)?t:e.name})}function v(e){let t=Object.assign({},e);for(let e in t)void 0===t[e]&&delete t[e];return t}function b(e){let t=arguments.length>1&&void 0!==arguments[1]?arguments[1]:[],r=Object.assign({},e);for(let e of t)e in r&&delete r[e];return r}let y=(0,s.createContext)(null);y.displayName="OpenClosedContext";var E=((i=E||{})[i.Open=1]="Open",i[i.Closed=2]="Closed",i[i.Closing=4]="Closing",i[i.Opening=8]="Opening",i);function x(){return(0,s.useContext)(y)}function w(e){let{value:t,children:r}=e;return s.createElement(y.Provider,{value:t},r)}var C=Object.defineProperty,O=(e,t,r)=>t in e?C(e,t,{enumerable:!0,configurable:!0,writable:!0,value:r}):e[t]=r,N=(e,t,r)=>(O(e,"symbol"!=typeof t?t+"":t,r),r);class F{set(e){this.current!==e&&(this.handoffState="pending",this.currentId=0,this.current=e)}reset(){this.set(this.detect())}nextId(){return++this.currentId}get isServer(){return"server"===this.current}get isClient(){return"client"===this.current}detect(){return"undefined"==typeof window||"undefined"==typeof document?"server":"client"}handoff(){"pending"===this.handoffState&&(this.handoffState="complete")}get isHandoffComplete(){return"complete"===this.handoffState}constructor(){N(this,"current",this.detect()),N(this,"handoffState","pending"),N(this,"currentId",0)}}let T=new F,A=(e,t)=>{T.isServer?(0,s.useEffect)(e,t):(0,s.useLayoutEffect)(e,t)};function S(){let e=(0,s.useRef)(!1);return A(()=>(e.current=!0,()=>{e.current=!1}),[]),e}function j(e){let t=(0,s.useRef)(e);return A(()=>{t.current=e},[e]),t}function k(){let e;let t=(e="undefined"==typeof document,(0,l.useSyncExternalStore)(()=>()=>{},()=>!1,()=>!e)),[r,n]=s.useState(T.isHandoffComplete);return r&&!1===T.isHandoffComplete&&n(!1),s.useEffect(()=>{!0!==r&&n(!0)},[r]),s.useEffect(()=>T.handoff(),[]),!t&&r}let P=function(e){let t=j(e);return s.useCallback(function(){for(var e=arguments.length,r=Array(e),n=0;n<e;n++)r[n]=arguments[n];return t.current(...r)},[t])},$=Symbol();function L(){for(var e=arguments.length,t=Array(e),r=0;r<e;r++)t[r]=arguments[r];let n=(0,s.useRef)(t);(0,s.useEffect)(()=>{n.current=t},[t]);let a=P(e=>{for(let t of n.current)null!=t&&("function"==typeof t?t(e):t.current=e)});return t.every(e=>null==e||(null==e?void 0:e[$]))?void 0:a}function R(){let e=[],t={addEventListener:(e,r,n,a)=>(e.addEventListener(r,n,a),t.add(()=>e.removeEventListener(r,n,a))),requestAnimationFrame(){for(var e=arguments.length,r=Array(e),n=0;n<e;n++)r[n]=arguments[n];let a=requestAnimationFrame(...r);return t.add(()=>cancelAnimationFrame(a))},nextFrame(){for(var e=arguments.length,r=Array(e),n=0;n<e;n++)r[n]=arguments[n];return t.requestAnimationFrame(()=>t.requestAnimationFrame(...r))},setTimeout(){for(var e=arguments.length,r=Array(e),n=0;n<e;n++)r[n]=arguments[n];let a=setTimeout(...r);return t.add(()=>clearTimeout(a))},microTask(){for(var e,r=arguments.length,n=Array(r),a=0;a<r;a++)n[a]=arguments[a];let i={current:!0};return e=()=>{i.current&&n[0]()},"function"==typeof queueMicrotask?queueMicrotask(e):Promise.resolve().then(e).catch(e=>setTimeout(()=>{throw e})),t.add(()=>{i.current=!1})},style(e,t,r){let n=e.style.getPropertyValue(t);return Object.assign(e.style,{[t]:r}),this.add(()=>{Object.assign(e.style,{[t]:n})})},group(e){let t=R();return e(t),this.add(()=>t.dispose())},add:t=>(e.push(t),()=>{let r=e.indexOf(t);if(r>=0)for(let t of e.splice(r,1))t()}),dispose(){for(let t of e.splice(0))t()}};return t}function H(e){for(var t=arguments.length,r=Array(t>1?t-1:0),n=1;n<t;n++)r[n-1]=arguments[n];e&&r.length>0&&e.classList.add(...r)}function D(e){for(var t=arguments.length,r=Array(t>1?t-1:0),n=1;n<t;n++)r[n-1]=arguments[n];e&&r.length>0&&e.classList.remove(...r)}function I(){let[e]=(0,s.useState)(R);return(0,s.useEffect)(()=>()=>e.dispose(),[e]),e}function M(){let e=arguments.length>0&&void 0!==arguments[0]?arguments[0]:"";return e.split(" ").filter(e=>e.trim().length>1)}let z=(0,s.createContext)(null);z.displayName="TransitionContext";var q=((o=q||{}).Visible="visible",o.Hidden="hidden",o);let U=(0,s.createContext)(null);function _(e){return"children"in e?_(e.children):e.current.filter(e=>{let{el:t}=e;return null!==t.current}).filter(e=>{let{state:t}=e;return"visible"===t}).length>0}function B(e,t){let r=j(e),n=(0,s.useRef)([]),a=S(),i=I(),o=P(function(e){let t=arguments.length>1&&void 0!==arguments[1]?arguments[1]:f.Hidden,o=n.current.findIndex(t=>{let{el:r}=t;return r===e});-1!==o&&(c(t,{[f.Unmount](){n.current.splice(o,1)},[f.Hidden](){n.current[o].state="hidden"}}),i.microTask(()=>{var e;!_(n)&&a.current&&(null==(e=r.current)||e.call(r))}))}),l=P(e=>{let t=n.current.find(t=>{let{el:r}=t;return r===e});return t?"visible"!==t.state&&(t.state="visible"):n.current.push({el:e,state:"visible"}),()=>o(e,f.Unmount)}),u=(0,s.useRef)([]),d=(0,s.useRef)(Promise.resolve()),p=(0,s.useRef)({enter:[],leave:[],idle:[]}),m=P((e,r,n)=>{u.current.splice(0),t&&(t.chains.current[r]=t.chains.current[r].filter(t=>{let[r]=t;return r!==e})),null==t||t.chains.current[r].push([e,new Promise(e=>{u.current.push(e)})]),null==t||t.chains.current[r].push([e,new Promise(e=>{Promise.all(p.current[r].map(e=>{let[t,r]=e;return r})).then(()=>e())})]),"enter"===r?d.current=d.current.then(()=>null==t?void 0:t.wait.current).then(()=>n(r)):n(r)}),h=P((e,t,r)=>{Promise.all(p.current[t].splice(0).map(e=>{let[t,r]=e;return r})).then(()=>{var e;null==(e=u.current.shift())||e()}).then(()=>r(t))});return(0,s.useMemo)(()=>({children:n,register:l,unregister:o,onStart:m,onStop:h,wait:d,chains:p}),[l,o,n,m,h,p,d])}function V(){}U.displayName="NestingContext";let Y=["beforeEnter","afterEnter","beforeLeave","afterLeave"];function Z(e){var t;let r={};for(let n of Y)r[n]=null!=(t=e[n])?t:V;return r}let W=d.RenderStrategy,G=g(function(e,t){let{show:r,appear:n=!1,unmount:a=!0,...i}=e,o=(0,s.useRef)(null),l=L(o,t);k();let u=x();if(void 0===r&&null!==u&&(r=(u&E.Open)===E.Open),![!0,!1].includes(r))throw Error("A <Transition /> is used but it is missing a `show={true | false}` prop.");let[c,d]=(0,s.useState)(r?"visible":"hidden"),f=B(()=>{d("hidden")}),[m,h]=(0,s.useState)(!0),g=(0,s.useRef)([r]);A(()=>{!1!==m&&g.current[g.current.length-1]!==r&&(g.current.push(r),h(!1))},[g,r]);let v=(0,s.useMemo)(()=>({show:r,appear:n,initial:m}),[r,n,m]);(0,s.useEffect)(()=>{if(r)d("visible");else if(_(f)){let e=o.current;if(!e)return;let t=e.getBoundingClientRect();0===t.x&&0===t.y&&0===t.width&&0===t.height&&d("hidden")}else d("hidden")},[r,f]);let b={unmount:a},y=P(()=>{var t;m&&h(!1),null==(t=e.beforeEnter)||t.call(e)}),w=P(()=>{var t;m&&h(!1),null==(t=e.beforeLeave)||t.call(e)});return s.createElement(U.Provider,{value:f},s.createElement(z.Provider,{value:v},p({ourProps:{...b,as:s.Fragment,children:s.createElement(J,{ref:l,...b,...i,beforeEnter:y,beforeLeave:w})},theirProps:{},defaultTag:s.Fragment,features:W,visible:"visible"===c,name:"Transition"})))}),J=g(function(e,t){var r,n,a;let i;let{beforeEnter:o,afterEnter:l,beforeLeave:d,afterLeave:m,enter:h,enterFrom:g,enterTo:v,entered:b,leave:y,leaveFrom:x,leaveTo:C,...O}=e,N=(0,s.useRef)(null),F=L(N,t),T=null==(r=O.unmount)||r?f.Unmount:f.Hidden,{show:$,appear:q,initial:V}=function(){let e=(0,s.useContext)(z);if(null===e)throw Error("A <Transition.Child /> is used but it is missing a parent <Transition /> or <Transition.Root />.");return e}(),[Y,G]=(0,s.useState)($?"visible":"hidden"),J=function(){let e=(0,s.useContext)(U);if(null===e)throw Error("A <Transition.Child /> is used but it is missing a parent <Transition /> or <Transition.Root />.");return e}(),{register:K,unregister:Q}=J;(0,s.useEffect)(()=>K(N),[K,N]),(0,s.useEffect)(()=>{if(T===f.Hidden&&N.current){if($&&"visible"!==Y){G("visible");return}return c(Y,{hidden:()=>Q(N),visible:()=>K(N)})}},[Y,N,K,Q,$,T]);let X=j({base:M(O.className),enter:M(h),enterFrom:M(g),enterTo:M(v),entered:M(b),leave:M(y),leaveFrom:M(x),leaveTo:M(C)}),ee=(a={beforeEnter:o,afterEnter:l,beforeLeave:d,afterLeave:m},i=(0,s.useRef)(Z(a)),(0,s.useEffect)(()=>{i.current=Z(a)},[a]),i),et=k();(0,s.useEffect)(()=>{if(et&&"visible"===Y&&null===N.current)throw Error("Did you forget to passthrough the `ref` to the actual DOM node?")},[N,Y,et]);let er=q&&$&&V,en=et&&(!V||q)?$?"enter":"leave":"idle",ea=function(){let e=arguments.length>0&&void 0!==arguments[0]?arguments[0]:0,[t,r]=(0,s.useState)(e),n=S(),a=(0,s.useCallback)(e=>{n.current&&r(t=>t|e)},[t,n]),i=(0,s.useCallback)(e=>!!(t&e),[t]);return{flags:t,addFlag:a,hasFlag:i,removeFlag:(0,s.useCallback)(e=>{n.current&&r(t=>t&~e)},[r,n]),toggleFlag:(0,s.useCallback)(e=>{n.current&&r(t=>t^e)},[r])}}(0),ei=P(e=>c(e,{enter:()=>{ea.addFlag(E.Opening),ee.current.beforeEnter()},leave:()=>{ea.addFlag(E.Closing),ee.current.beforeLeave()},idle:()=>{}})),eo=P(e=>c(e,{enter:()=>{ea.removeFlag(E.Opening),ee.current.afterEnter()},leave:()=>{ea.removeFlag(E.Closing),ee.current.afterLeave()},idle:()=>{}})),es=B(()=>{G("hidden"),Q(N)},J);!function(e){let{immediate:t,container:r,direction:n,classes:a,onStart:i,onStop:o}=e,s=S(),l=I(),u=j(n);A(()=>{t&&(u.current="enter")},[t]),A(()=>{let e=R();l.add(e.dispose);let t=r.current;if(t&&"idle"!==u.current&&s.current){var n,d,f;let r,s,l,p,m,h,g;return e.dispose(),i.current(u.current),e.add((n=a.current,d="enter"===u.current,f=()=>{e.dispose(),o.current(u.current)},s=d?"enter":"leave",l=R(),p=void 0!==f?(r={called:!1},function(){for(var e=arguments.length,t=Array(e),n=0;n<e;n++)t[n]=arguments[n];if(!r.called)return r.called=!0,f(...t)}):()=>{},"enter"===s&&(t.removeAttribute("hidden"),t.style.display=""),m=c(s,{enter:()=>n.enter,leave:()=>n.leave}),h=c(s,{enter:()=>n.enterTo,leave:()=>n.leaveTo}),g=c(s,{enter:()=>n.enterFrom,leave:()=>n.leaveFrom}),D(t,...n.base,...n.enter,...n.enterTo,...n.enterFrom,...n.leave,...n.leaveFrom,...n.leaveTo,...n.entered),H(t,...n.base,...m,...g),l.nextFrame(()=>{D(t,...n.base,...m,...g),H(t,...n.base,...m,...h),function(e,t){let r=R();if(!e)return r.dispose;let{transitionDuration:n,transitionDelay:a}=getComputedStyle(e),[i,o]=[n,a].map(e=>{let[t=0]=e.split(",").filter(Boolean).map(e=>e.includes("ms")?parseFloat(e):1e3*parseFloat(e)).sort((e,t)=>t-e);return t}),s=i+o;if(0!==s){r.group(r=>{r.setTimeout(()=>{t(),r.dispose()},s),r.addEventListener(e,"transitionrun",e=>{e.target===e.currentTarget&&r.dispose()})});let n=r.addEventListener(e,"transitionend",e=>{e.target===e.currentTarget&&(t(),n())})}else t();r.add(()=>t()),r.dispose}(t,()=>(D(t,...n.base,...m),H(t,...n.base,...n.entered),p()))}),l.dispose)),e.dispose}},[n])}({immediate:er,container:N,classes:X,direction:en,onStart:j(e=>{es.onStart(N,e,ei)}),onStop:j(e=>{es.onStop(N,e,eo),"leave"!==e||_(es)||(G("hidden"),Q(N))})});let el=O;return er?el={...el,className:u(O.className,...X.current.enter,...X.current.enterFrom)}:(el.className=u(O.className,null==(n=N.current)?void 0:n.className),""===el.className&&delete el.className),s.createElement(U.Provider,{value:es},s.createElement(w,{value:c(Y,{visible:E.Open,hidden:E.Closed})|ea.flags},p({ourProps:{ref:F},theirProps:el,defaultTag:"div",features:W,visible:"visible"===Y,name:"Transition.Child"})))}),K=g(function(e,t){let r=null!==(0,s.useContext)(z),n=null!==x();return s.createElement(s.Fragment,null,!r&&n?s.createElement(G,{ref:t,...e}):s.createElement(J,{ref:t,...e}))}),Q=Object.assign(G,{Child:K,Root:G})},1386:function(e,t,r){let n,a;r.d(t,{x7:function(){return ed},ZP:function(){return ef}});var i,o=r(78346);let s={data:""},l=e=>"object"==typeof window?((e?e.querySelector("#_goober"):window._goober)||Object.assign((e||document.head).appendChild(document.createElement("style")),{innerHTML:" ",id:"_goober"})).firstChild:e||s,u=/(?:([\u0080-\uFFFF\w-%@]+) *:? *([^{;]+?);|([^;}{]*?) *{)|(}\s*)/g,c=/\/\*[^]*?\*\/|  +/g,d=/\n+/g,f=(e,t)=>{let r="",n="",a="";for(let i in e){let o=e[i];"@"==i[0]?"i"==i[1]?r=i+" "+o+";":n+="f"==i[1]?f(o,i):i+"{"+f(o,"k"==i[1]?"":t)+"}":"object"==typeof o?n+=f(o,t?t.replace(/([^,])+/g,e=>i.replace(/(^:.*)|([^,])+/g,t=>/&/.test(t)?t.replace(/&/g,e):e?e+" "+t:t)):i):null!=o&&(i=/^--/.test(i)?i:i.replace(/[A-Z]/g,"-$&").toLowerCase(),a+=f.p?f.p(i,o):i+":"+o+";")}return r+(t&&a?t+"{"+a+"}":a)+n},p={},m=e=>{if("object"==typeof e){let t="";for(let r in e)t+=r+m(e[r]);return t}return e},h=(e,t,r,n,a)=>{var i;let o=m(e),s=p[o]||(p[o]=(e=>{let t=0,r=11;for(;t<e.length;)r=101*r+e.charCodeAt(t++)>>>0;return"go"+r})(o));if(!p[s]){let t=o!==e?e:(e=>{let t,r,n=[{}];for(;t=u.exec(e.replace(c,""));)t[4]?n.shift():t[3]?(r=t[3].replace(d," ").trim(),n.unshift(n[0][r]=n[0][r]||{})):n[0][t[1]]=t[2].replace(d," ").trim();return n[0]})(e);p[s]=f(a?{["@keyframes "+s]:t}:t,r?"":"."+s)}let l=r&&p.g?p.g:null;return r&&(p.g=p[s]),i=p[s],l?t.data=t.data.replace(l,i):-1===t.data.indexOf(i)&&(t.data=n?i+t.data:t.data+i),s},g=(e,t,r)=>e.reduce((e,n,a)=>{let i=t[a];if(i&&i.call){let e=i(r),t=e&&e.props&&e.props.className||/^go/.test(e)&&e;i=t?"."+t:e&&"object"==typeof e?e.props?"":f(e,""):!1===e?"":e}return e+n+(null==i?"":i)},"");function v(e){let t=this||{},r=e.call?e(t.p):e;return h(r.unshift?r.raw?g(r,[].slice.call(arguments,1),t.p):r.reduce((e,r)=>Object.assign(e,r&&r.call?r(t.p):r),{}):r,l(t.target),t.g,t.o,t.k)}v.bind({g:1});let b,y,E,x=v.bind({k:1});function w(e,t){let r=this||{};return function(){let n=arguments;function a(i,o){let s=Object.assign({},i),l=s.className||a.className;r.p=Object.assign({theme:y&&y()},s),r.o=/ *go\d+/.test(l),s.className=v.apply(r,n)+(l?" "+l:""),t&&(s.ref=o);let u=e;return e[0]&&(u=s.as||e,delete s.as),E&&u[0]&&E(s),b(u,s)}return t?t(a):a}}var C=e=>"function"==typeof e,O=(e,t)=>C(e)?e(t):e,N=(n=0,()=>(++n).toString()),F=()=>{if(void 0===a&&"u">typeof window){let e=matchMedia("(prefers-reduced-motion: reduce)");a=!e||e.matches}return a},T=new Map,A=e=>{if(T.has(e))return;let t=setTimeout(()=>{T.delete(e),$({type:4,toastId:e})},1e3);T.set(e,t)},S=e=>{let t=T.get(e);t&&clearTimeout(t)},j=(e,t)=>{switch(t.type){case 0:return{...e,toasts:[t.toast,...e.toasts].slice(0,20)};case 1:return t.toast.id&&S(t.toast.id),{...e,toasts:e.toasts.map(e=>e.id===t.toast.id?{...e,...t.toast}:e)};case 2:let{toast:r}=t;return e.toasts.find(e=>e.id===r.id)?j(e,{type:1,toast:r}):j(e,{type:0,toast:r});case 3:let{toastId:n}=t;return n?A(n):e.toasts.forEach(e=>{A(e.id)}),{...e,toasts:e.toasts.map(e=>e.id===n||void 0===n?{...e,visible:!1}:e)};case 4:return void 0===t.toastId?{...e,toasts:[]}:{...e,toasts:e.toasts.filter(e=>e.id!==t.toastId)};case 5:return{...e,pausedAt:t.time};case 6:let a=t.time-(e.pausedAt||0);return{...e,pausedAt:void 0,toasts:e.toasts.map(e=>({...e,pauseDuration:e.pauseDuration+a}))}}},k=[],P={toasts:[],pausedAt:void 0},$=e=>{P=j(P,e),k.forEach(e=>{e(P)})},L={blank:4e3,error:4e3,success:2e3,loading:1/0,custom:4e3},R=function(){let e=arguments.length>0&&void 0!==arguments[0]?arguments[0]:{},[t,r]=(0,o.useState)(P);(0,o.useEffect)(()=>(k.push(r),()=>{let e=k.indexOf(r);e>-1&&k.splice(e,1)}),[t]);let n=t.toasts.map(t=>{var r,n;return{...e,...e[t.type],...t,duration:t.duration||(null==(r=e[t.type])?void 0:r.duration)||(null==e?void 0:e.duration)||L[t.type],style:{...e.style,...null==(n=e[t.type])?void 0:n.style,...t.style}}});return{...t,toasts:n}},H=function(e){let t=arguments.length>1&&void 0!==arguments[1]?arguments[1]:"blank",r=arguments.length>2?arguments[2]:void 0;return{createdAt:Date.now(),visible:!0,type:t,ariaProps:{role:"status","aria-live":"polite"},message:e,pauseDuration:0,...r,id:(null==r?void 0:r.id)||N()}},D=e=>(t,r)=>{let n=H(t,e,r);return $({type:2,toast:n}),n.id},I=(e,t)=>D("blank")(e,t);I.error=D("error"),I.success=D("success"),I.loading=D("loading"),I.custom=D("custom"),I.dismiss=e=>{$({type:3,toastId:e})},I.remove=e=>$({type:4,toastId:e}),I.promise=(e,t,r)=>{let n=I.loading(t.loading,{...r,...null==r?void 0:r.loading});return e.then(e=>(I.success(O(t.success,e),{id:n,...r,...null==r?void 0:r.success}),e)).catch(e=>{I.error(O(t.error,e),{id:n,...r,...null==r?void 0:r.error})}),e};var M=(e,t)=>{$({type:1,toast:{id:e,height:t}})},z=()=>{$({type:5,time:Date.now()})},q=e=>{let{toasts:t,pausedAt:r}=R(e);(0,o.useEffect)(()=>{if(r)return;let e=Date.now(),n=t.map(t=>{if(t.duration===1/0)return;let r=(t.duration||0)+t.pauseDuration-(e-t.createdAt);if(r<0){t.visible&&I.dismiss(t.id);return}return setTimeout(()=>I.dismiss(t.id),r)});return()=>{n.forEach(e=>e&&clearTimeout(e))}},[t,r]);let n=(0,o.useCallback)(()=>{r&&$({type:6,time:Date.now()})},[r]),a=(0,o.useCallback)((e,r)=>{let{reverseOrder:n=!1,gutter:a=8,defaultPosition:i}=r||{},o=t.filter(t=>(t.position||i)===(e.position||i)&&t.height),s=o.findIndex(t=>t.id===e.id),l=o.filter((e,t)=>t<s&&e.visible).length;return o.filter(e=>e.visible).slice(...n?[l+1]:[0,l]).reduce((e,t)=>e+(t.height||0)+a,0)},[t]);return{toasts:t,handlers:{updateHeight:M,startPause:z,endPause:n,calculateOffset:a}}},U=x`
from {
  transform: scale(0) rotate(45deg);
	opacity: 0;
}
to {
 transform: scale(1) rotate(45deg);
  opacity: 1;
}`,_=x`
from {
  transform: scale(0);
  opacity: 0;
}
to {
  transform: scale(1);
  opacity: 1;
}`,B=x`
from {
  transform: scale(0) rotate(90deg);
	opacity: 0;
}
to {
  transform: scale(1) rotate(90deg);
	opacity: 1;
}`,V=w("div")`
  width: 20px;
  opacity: 0;
  height: 20px;
  border-radius: 10px;
  background: ${e=>e.primary||"#ff4b4b"};
  position: relative;
  transform: rotate(45deg);

  animation: ${U} 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275)
    forwards;
  animation-delay: 100ms;

  &:after,
  &:before {
    content: '';
    animation: ${_} 0.15s ease-out forwards;
    animation-delay: 150ms;
    position: absolute;
    border-radius: 3px;
    opacity: 0;
    background: ${e=>e.secondary||"#fff"};
    bottom: 9px;
    left: 4px;
    height: 2px;
    width: 12px;
  }

  &:before {
    animation: ${B} 0.15s ease-out forwards;
    animation-delay: 180ms;
    transform: rotate(90deg);
  }
`,Y=x`
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
`,Z=w("div")`
  width: 12px;
  height: 12px;
  box-sizing: border-box;
  border: 2px solid;
  border-radius: 100%;
  border-color: ${e=>e.secondary||"#e0e0e0"};
  border-right-color: ${e=>e.primary||"#616161"};
  animation: ${Y} 1s linear infinite;
`,W=x`
from {
  transform: scale(0) rotate(45deg);
	opacity: 0;
}
to {
  transform: scale(1) rotate(45deg);
	opacity: 1;
}`,G=x`
0% {
	height: 0;
	width: 0;
	opacity: 0;
}
40% {
  height: 0;
	width: 6px;
	opacity: 1;
}
100% {
  opacity: 1;
  height: 10px;
}`,J=w("div")`
  width: 20px;
  opacity: 0;
  height: 20px;
  border-radius: 10px;
  background: ${e=>e.primary||"#61d345"};
  position: relative;
  transform: rotate(45deg);

  animation: ${W} 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275)
    forwards;
  animation-delay: 100ms;
  &:after {
    content: '';
    box-sizing: border-box;
    animation: ${G} 0.2s ease-out forwards;
    opacity: 0;
    animation-delay: 200ms;
    position: absolute;
    border-right: 2px solid;
    border-bottom: 2px solid;
    border-color: ${e=>e.secondary||"#fff"};
    bottom: 6px;
    left: 6px;
    height: 10px;
    width: 6px;
  }
`,K=w("div")`
  position: absolute;
`,Q=w("div")`
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
  min-width: 20px;
  min-height: 20px;
`,X=x`
from {
  transform: scale(0.6);
  opacity: 0.4;
}
to {
  transform: scale(1);
  opacity: 1;
}`,ee=w("div")`
  position: relative;
  transform: scale(0.6);
  opacity: 0.4;
  min-width: 20px;
  animation: ${X} 0.3s 0.12s cubic-bezier(0.175, 0.885, 0.32, 1.275)
    forwards;
`,et=e=>{let{toast:t}=e,{icon:r,type:n,iconTheme:a}=t;return void 0!==r?"string"==typeof r?o.createElement(ee,null,r):r:"blank"===n?null:o.createElement(Q,null,o.createElement(Z,{...a}),"loading"!==n&&o.createElement(K,null,"error"===n?o.createElement(V,{...a}):o.createElement(J,{...a})))},er=e=>`
0% {transform: translate3d(0,${-200*e}%,0) scale(.6); opacity:.5;}
100% {transform: translate3d(0,0,0) scale(1); opacity:1;}
`,en=e=>`
0% {transform: translate3d(0,0,-1px) scale(1); opacity:1;}
100% {transform: translate3d(0,${-150*e}%,-1px) scale(.6); opacity:0;}
`,ea=w("div")`
  display: flex;
  align-items: center;
  background: #fff;
  color: #363636;
  line-height: 1.3;
  will-change: transform;
  box-shadow: 0 3px 10px rgba(0, 0, 0, 0.1), 0 3px 3px rgba(0, 0, 0, 0.05);
  max-width: 350px;
  pointer-events: auto;
  padding: 8px 10px;
  border-radius: 8px;
`,ei=w("div")`
  display: flex;
  justify-content: center;
  margin: 4px 10px;
  color: inherit;
  flex: 1 1 auto;
  white-space: pre-line;
`,eo=(e,t)=>{let r=e.includes("top")?1:-1,[n,a]=F()?["0%{opacity:0;} 100%{opacity:1;}","0%{opacity:1;} 100%{opacity:0;}"]:[er(r),en(r)];return{animation:t?`${x(n)} 0.35s cubic-bezier(.21,1.02,.73,1) forwards`:`${x(a)} 0.4s forwards cubic-bezier(.06,.71,.55,1)`}},es=o.memo(e=>{let{toast:t,position:r,style:n,children:a}=e,i=t.height?eo(t.position||r||"top-center",t.visible):{opacity:0},s=o.createElement(et,{toast:t}),l=o.createElement(ei,{...t.ariaProps},O(t.message,t));return o.createElement(ea,{className:t.className,style:{...i,...n,...t.style}},"function"==typeof a?a({icon:s,message:l}):o.createElement(o.Fragment,null,s,l))});i=o.createElement,f.p=void 0,b=i,y=void 0,E=void 0;var el=e=>{let{id:t,className:r,style:n,onHeightUpdate:a,children:i}=e,s=o.useCallback(e=>{if(e){let r=()=>{a(t,e.getBoundingClientRect().height)};r(),new MutationObserver(r).observe(e,{subtree:!0,childList:!0,characterData:!0})}},[t,a]);return o.createElement("div",{ref:s,className:r,style:n},i)},eu=(e,t)=>{let r=e.includes("top"),n=e.includes("center")?{justifyContent:"center"}:e.includes("right")?{justifyContent:"flex-end"}:{};return{left:0,right:0,display:"flex",position:"absolute",transition:F()?void 0:"all 230ms cubic-bezier(.21,1.02,.73,1)",transform:`translateY(${t*(r?1:-1)}px)`,...r?{top:0}:{bottom:0},...n}},ec=v`
  z-index: 9999;
  > * {
    pointer-events: auto;
  }
`,ed=e=>{let{reverseOrder:t,position:r="top-center",toastOptions:n,gutter:a,children:i,containerStyle:s,containerClassName:l}=e,{toasts:u,handlers:c}=q(n);return o.createElement("div",{style:{position:"fixed",zIndex:9999,top:16,left:16,right:16,bottom:16,pointerEvents:"none",...s},className:l,onMouseEnter:c.startPause,onMouseLeave:c.endPause},u.map(e=>{let n=e.position||r,s=eu(n,c.calculateOffset(e,{reverseOrder:t,gutter:a,defaultPosition:r}));return o.createElement(el,{id:e.id,key:e.id,onHeightUpdate:c.updateHeight,className:e.visible?ec:"",style:s},"custom"===e.type?O(e.message,e):i?i(e):o.createElement(es,{toast:e,position:n}))}))},ef=I}}]);