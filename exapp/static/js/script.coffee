$(document).ready ->
  $(".nav li").removeClass("active").find("a[href='#{window.location.pathname}']").closest("li").addClass("active")



$(".action_button").live
  click: (e)->
    e.preventDefault()
    if $(@).attr("action") == "mark_as_claimed"
      $("[name='mark_as']").val "True"
    else if $(@).attr("action") == "rejected"
      $("[name='mark_as']").val "rejected"


    selected_claims = ""
    for cb in $(".cb_claims")
      if $(cb).attr("checked")
        selected_claims += cb.id+";"
    selected_claims = selected_claims.substr(0, selected_claims.length-1)

    $("[name='selected']").val selected_claims
    $(@).closest('form').submit()

    #$(".mark_as_claimed").live
    #  click: (e)->
    #    e.preventDefault()
    #    $("[name='mark_as']").val "True"
    #    selected_claims = ""
    #    for cb in $(".cb_claims")
    #      if $(cb).attr("checked")
    #        selected_claims += cb.id+";"
    #    selected_claims = selected_claims.substr(0, selected_claims.length-1)
    #
    #    $("[name='selected']").val selected_claims
    #    $(@).closest('form').submit()
    #
    #
    #$(".rejected").live
    #  click: (e)->
    #    e.preventDefault()
    #    $("[name='mark_as']").val "rejected"
    #    selected_claims = ""
    #    for cb in $(".cb_claims")
    #      if $(cb).attr("checked")
    #        selected_claims += cb.id+";"
    #    selected_claims = selected_claims.substr(0, selected_claims.length-1)
    #
    #    $("[name='selected']").val selected_claims
    #    $(@).closest('form').submit()
    #
    #$(".mark_as_not_claimed").live
    #  click: (e)->
    #    e.preventDefault()
    #    $("[name='mark_as']").val "False"
    #    selected_claims = ""
    #    for cb in $(".cb_claims")
    #      if $(cb).attr("checked")
    #        selected_claims += cb.id+";"
    #    selected_claims = selected_claims.substr(0, selected_claims.length-1)
    #
    #    $("[name='selected']").val selected_claims
    #    $(@).closest('form').submit()

$("#check_all").live
  click: ->
    if $(@).attr "checked"
      $("[type='checkbox']").attr("checked", "checked")
    else
      $("[type='checkbox']").removeAttr("checked")
