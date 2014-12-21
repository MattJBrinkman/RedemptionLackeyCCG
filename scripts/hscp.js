function AddAndGo( cookieName, title, url ) {
    if (!GetCookie( cookieName )) {
			  if ( window.confirm( "Would you like to automatically bookmark the site you are going to?" )) {
			 		  DoCookie( cookieName );
						CreateBookmarkLink( title, url );
			  }
		} else {
		    DoCookie( cookieName );
				location.href = url;
		}
}

function CreateBookmarkLink(title, url) {
    if (window.sidebar) {
		// Mozilla Firefox Bookmark
				location.href = url;
		    window.alert("When site appears press CTRL-D to bookmark it.");
//		    window.sidebar.addPanel(title, url,"");
    }
		else if( window.external ) {
		// IE Favorite
		    window.external.AddFavorite( url, title);
				location.href = url;
		}
		else if(window.opera && window.print) {
		// Opera Hotlist
				location.href = url;
		    return true;
		}
 }
 
function SetCookie ( name, value, expYear, expMonth, expDay, path, domain, secure )
{
    var cookieString = name + "=" + escape ( value );

    if ( expYear ) {
		    var expires = new Date ( expYear, expMonth, expDay );
				cookieString += "; expires=" + expires.toGMTString();
    }

    if ( path ) {
        cookieString += "; path=" + escape ( path );
		}

    if ( domain ) {
        cookieString += "; domain=" + escape ( domain );
		}
		  
    if ( secure ) {
        cookieString += "; secure";
		}
  
    document.cookie = cookieString;
}

function DeleteCookie ( cookieName )
{
    var cookieDate = new Date ( );  // current date & time
    cookieDate.setTime ( cookieDate.getTime() - 1 );
    document.cookie = cookieName += "=; expires=" + cookieDate.toGMTString();
}

function GetCookie ( cookieName )
{
    var results = document.cookie.match ( '(^|;) ?' + cookieName + '=([^;]*)(;|$)' );

    if ( results ) {
        return ( unescape ( results[2] ) );
		}
    else {
        return null;
		}
}

function DoCookie(cookieName) {
    var currentDate = new Date;
    var cookieYear = currentDate.getFullYear ( ) + 1;
    var cookieMonth = currentDate.getMonth ( );
    var cookieDay = currentDate.getDate ( );
		SetCookie(cookieName, "set", cookieYear, cookieMonth, cookieDay);
}

